#!/usr/bin/env python3
"""
Automated Knowledge Graph Generator for Category Theory Documents
Uses spaCy for NLP processing and NetworkX for graph construction
"""

import os
import re
import spacy
import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from collections import defaultdict, Counter
from pathlib import Path
import json
from typing import List, Dict, Tuple, Set
import argparse

class CategoryTheoryKG:
    def __init__(self, docs_path: str, output_path: str = "knowledge-graph"):
        self.docs_path = Path(docs_path)
        self.output_path = Path(output_path)
        self.output_path.mkdir(exist_ok=True)
        
        # Load spaCy model
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except OSError:
            print("Please install spaCy English model: python -m spacy download en_core_web_sm")
            raise
        
        # Category theory vocabulary
        self.math_terms = {
            # Core concepts
            "category", "functor", "morphism", "object", "composition",
            "identity", "natural transformation", "adjunction", "limit", "colimit",
            
            # Specific structures
            "monad", "comonad", "algebra", "coalgebra", "monoid", "group",
            "homomorphism", "isomorphism", "endomorphism", "automorphism",
            
            # Advanced concepts
            "topos", "sheaf", "presheaf", "yoneda", "kan extension",
            "homotopy", "fibration", "opfibration", "cartesian", "cocartesian",
            
            # Optics and lenses
            "lens", "prism", "traversal", "iso", "optic", "profunctor",
            "store comonad", "van laarhoven",
            
            # Programming concepts
            "haskell", "type", "function", "lambda", "curry", "uncurry",
            "fold", "unfold", "catamorphism", "anamorphism",
            
            # Logic and foundations
            "proposition", "proof", "theorem", "axiom", "logic", "set theory"
        }
        
        # Initialize graph
        self.graph = nx.Graph()
        self.concept_frequency = Counter()
        self.document_concepts = defaultdict(set)
        self.concept_cooccurrence = defaultdict(lambda: defaultdict(int))
        
        # Add custom entity ruler for mathematical terms
        self._setup_custom_ner()
    
    def _setup_custom_ner(self):
        """Add custom entity recognition for mathematical terms"""
        if "entity_ruler" not in self.nlp.pipe_names:
            ruler = self.nlp.add_pipe("entity_ruler", before="ner")
        else:
            ruler = self.nlp.get_pipe("entity_ruler")
        
        # Create patterns for mathematical terms
        patterns = []
        for term in self.math_terms:
            patterns.append({"label": "MATH_CONCEPT", "pattern": term})
            # Also match capitalized versions
            patterns.append({"label": "MATH_CONCEPT", "pattern": term.title()})
            # Match plural forms
            if not term.endswith('s'):
                patterns.append({"label": "MATH_CONCEPT", "pattern": term + "s"})
        
        ruler.add_patterns(patterns)
    
    def extract_markdown_concepts(self, text: str) -> Set[str]:
        """Extract concepts from markdown links and headers"""
        concepts = set()
        
        # Extract from markdown links [[concept]]
        wiki_links = re.findall(r'\[\[([^\]]+)\]\]', text)
        concepts.update(link.lower().strip() for link in wiki_links)
        
        # Extract from headers
        headers = re.findall(r'^#+\s+(.+)$', text, re.MULTILINE)
        for header in headers:
            # Clean header text
            clean_header = re.sub(r'[^\w\s]', '', header).lower().strip()
            if len(clean_header) > 2:
                concepts.add(clean_header)
        
        # Extract from code blocks (function names, types)
        code_blocks = re.findall(r'```(?:haskell|python|scala)?\n(.*?)\n```', text, re.DOTALL)
        for code in code_blocks:
            # Extract Haskell type signatures and function names
            type_sigs = re.findall(r'(\w+)\s*::', code)
            concepts.update(sig.lower() for sig in type_sigs)
        
        return concepts
    
    def process_document(self, file_path: Path) -> Dict[str, any]:
        """Process a single document and extract concepts"""
        print(f"Processing: {file_path.name}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
        
        # Extract markdown-specific concepts
        markdown_concepts = self.extract_markdown_concepts(text)
        
        # Process with spaCy
        doc = self.nlp(text)
        
        # Extract entities
        spacy_concepts = set()
        for ent in doc.ents:
            if ent.label_ in ["MATH_CONCEPT", "PERSON", "ORG"] or ent.text.lower() in self.math_terms:
                concept = ent.text.lower().strip()
                if len(concept) > 2:  # Filter out very short terms
                    spacy_concepts.add(concept)
        
        # Extract noun phrases that might be mathematical concepts
        noun_phrases = set()
        for chunk in doc.noun_chunks:
            chunk_text = chunk.text.lower().strip()
            if any(term in chunk_text for term in self.math_terms):
                noun_phrases.add(chunk_text)
        
        # Combine all concepts
        all_concepts = markdown_concepts | spacy_concepts | noun_phrases
        
        # Filter and clean concepts
        filtered_concepts = set()
        for concept in all_concepts:
            # Remove common stop words and very short terms
            if len(concept) > 2 and concept not in {'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'}:
                filtered_concepts.add(concept)
        
        # Store document concepts
        doc_name = file_path.stem
        self.document_concepts[doc_name] = filtered_concepts
        
        # Update concept frequency
        for concept in filtered_concepts:
            self.concept_frequency[concept] += 1
        
        # Calculate co-occurrence within this document
        concept_list = list(filtered_concepts)
        for i, concept1 in enumerate(concept_list):
            for concept2 in concept_list[i+1:]:
                self.concept_cooccurrence[concept1][concept2] += 1
                self.concept_cooccurrence[concept2][concept1] += 1
        
        return {
            'file': doc_name,
            'concepts': filtered_concepts,
            'concept_count': len(filtered_concepts),
            'word_count': len(doc)
        }
    
    def build_graph(self, min_frequency: int = 2, min_cooccurrence: int = 1):
        """Build the knowledge graph from extracted concepts"""
        print("Building knowledge graph...")
        
        # Add nodes (concepts that appear frequently enough)
        for concept, freq in self.concept_frequency.items():
            if freq >= min_frequency:
                self.graph.add_node(concept, 
                                  frequency=freq,
                                  type='concept',
                                  size=min(freq * 10, 100))
        
        # Add edges (co-occurrence relationships)
        for concept1, related_concepts in self.concept_cooccurrence.items():
            if concept1 in self.graph.nodes:
                for concept2, cooccur_count in related_concepts.items():
                    if (concept2 in self.graph.nodes and 
                        cooccur_count >= min_cooccurrence and 
                        concept1 != concept2):
                        
                        self.graph.add_edge(concept1, concept2,
                                          weight=cooccur_count,
                                          type='cooccurrence')
        
        print(f"Graph built: {self.graph.number_of_nodes()} nodes, {self.graph.number_of_edges()} edges")
    
    def analyze_graph(self) -> Dict[str, any]:
        """Analyze graph properties and find important concepts"""
        if self.graph.number_of_nodes() == 0:
            return {"error": "Empty graph"}
        
        # Calculate centrality measures
        degree_centrality = nx.degree_centrality(self.graph)
        betweenness_centrality = nx.betweenness_centrality(self.graph)
        closeness_centrality = nx.closeness_centrality(self.graph)
        
        # Find communities
        try:
            communities = list(nx.community.greedy_modularity_communities(self.graph))
        except:
            communities = []
        
        # Most important concepts
        top_concepts = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:10]
        
        return {
            'nodes': self.graph.number_of_nodes(),
            'edges': self.graph.number_of_edges(),
            'density': nx.density(self.graph),
            'top_concepts': top_concepts,
            'communities': len(communities),
            'centrality': {
                'degree': degree_centrality,
                'betweenness': betweenness_centrality,
                'closeness': closeness_centrality
            }
        }
    
    def visualize_static(self, output_file: str = "knowledge_graph.png"):
        """Create static visualization using matplotlib"""
        plt.figure(figsize=(20, 16))
        
        # Use spring layout for better visualization
        pos = nx.spring_layout(self.graph, k=3, iterations=50)
        
        # Node sizes based on frequency
        node_sizes = [self.graph.nodes[node].get('size', 20) for node in self.graph.nodes()]
        
        # Edge weights
        edge_weights = [self.graph.edges[edge].get('weight', 1) for edge in self.graph.edges()]
        
        # Draw the graph
        nx.draw_networkx_nodes(self.graph, pos, 
                              node_size=node_sizes,
                              node_color='lightblue',
                              alpha=0.7)
        
        nx.draw_networkx_edges(self.graph, pos,
                              width=[w * 0.5 for w in edge_weights],
                              alpha=0.5,
                              edge_color='gray')
        
        nx.draw_networkx_labels(self.graph, pos,
                               font_size=8,
                               font_weight='bold')
        
        plt.title("Category Theory Knowledge Graph", size=16, weight='bold')
        plt.axis('off')
        plt.tight_layout()
        
        output_path = self.output_path / output_file
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"Static visualization saved to: {output_path}")
    
    def visualize_interactive(self, output_file: str = "knowledge_graph.html"):
        """Create interactive visualization using Plotly"""
        if self.graph.number_of_nodes() == 0:
            print("Cannot visualize empty graph")
            return
        
        # Calculate layout
        pos = nx.spring_layout(self.graph, k=2, iterations=50)
        
        # Prepare edge traces
        edge_x = []
        edge_y = []
        edge_info = []
        
        for edge in self.graph.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])
            
            weight = self.graph.edges[edge].get('weight', 1)
            edge_info.append(f"{edge[0]} ↔ {edge[1]} (weight: {weight})")
        
        edge_trace = go.Scatter(x=edge_x, y=edge_y,
                               line=dict(width=0.5, color='#888'),
                               hoverinfo='none',
                               mode='lines')
        
        # Prepare node traces
        node_x = []
        node_y = []
        node_text = []
        node_info = []
        node_sizes = []
        
        for node in self.graph.nodes():
            x, y = pos[node]
            node_x.append(x)
            node_y.append(y)
            node_text.append(node)
            
            # Node info
            freq = self.graph.nodes[node].get('frequency', 1)
            degree = self.graph.degree[node]
            node_info.append(f"Concept: {node}<br>Frequency: {freq}<br>Connections: {degree}")
            node_sizes.append(max(10, freq * 5))
        
        node_trace = go.Scatter(x=node_x, y=node_y,
                               mode='markers+text',
                               hoverinfo='text',
                               text=node_text,
                               textposition="middle center",
                               hovertext=node_info,
                               marker=dict(size=node_sizes,
                                         color='lightblue',
                                         line=dict(width=2, color='darkblue')))
        
        # Create figure
        fig = go.Figure(data=[edge_trace, node_trace],
                       layout=go.Layout(
                           title=dict(text='Category Theory Knowledge Graph', font=dict(size=16)),
                           showlegend=False,
                           hovermode='closest',
                           margin=dict(b=20,l=5,r=5,t=40),
                           annotations=[ dict(
                               text="Hover over nodes for details",
                               showarrow=False,
                               xref="paper", yref="paper",
                               x=0.005, y=-0.002,
                               xanchor='left', yanchor='bottom',
                               font=dict(color='gray', size=12)
                           )],
                           xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                           yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                           plot_bgcolor='white'))
        
        output_path = self.output_path / output_file
        fig.write_html(str(output_path))
        
        print(f"Interactive visualization saved to: {output_path}")
    
    def visualize_3d(self, output_file: str = "knowledge_graph_3d.html"):
        """Create interactive 3D visualization using Plotly"""
        if self.graph.number_of_nodes() == 0:
            print("Cannot visualize empty graph")
            return
        
        # Calculate 3D layout using NetworkX spring layout with 3 dimensions
        pos_2d = nx.spring_layout(self.graph, k=2, iterations=50, dim=2)
        
        # Extend to 3D by adding z-coordinates based on graph properties
        pos_3d = {}
        degree_centrality = nx.degree_centrality(self.graph)
        betweenness_centrality = nx.betweenness_centrality(self.graph)
        
        for node in self.graph.nodes():
            x, y = pos_2d[node]
            # Use centrality measures to distribute nodes in 3D space
            z = (degree_centrality[node] + betweenness_centrality[node]) * 2 - 1
            pos_3d[node] = (x, y, z)
        
        # Prepare edge traces for 3D
        edge_x = []
        edge_y = []
        edge_z = []
        edge_info = []
        
        for edge in self.graph.edges():
            x0, y0, z0 = pos_3d[edge[0]]
            x1, y1, z1 = pos_3d[edge[1]]
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])
            edge_z.extend([z0, z1, None])
            
            weight = self.graph.edges[edge].get('weight', 1)
            edge_info.append(f"{edge[0]} ↔ {edge[1]} (weight: {weight})")
        
        edge_trace = go.Scatter3d(
            x=edge_x, y=edge_y, z=edge_z,
            line=dict(width=2, color='rgba(125,125,125,0.3)'),
            hoverinfo='none',
            mode='lines',
            name='Connections'
        )
        
        # Prepare node traces for 3D
        node_x = []
        node_y = []
        node_z = []
        node_text = []
        node_info = []
        node_sizes = []
        node_colors = []
        
        for node in self.graph.nodes():
            x, y, z = pos_3d[node]
            node_x.append(x)
            node_y.append(y)
            node_z.append(z)
            node_text.append(node)
            
            # Node info
            freq = self.graph.nodes[node].get('frequency', 1)
            degree = self.graph.degree[node]
            centrality = degree_centrality[node]
            
            node_info.append(
                f"<b>{node}</b><br>"
                f"Frequency: {freq}<br>"
                f"Connections: {degree}<br>"
                f"Centrality: {centrality:.3f}<br>"
                f"Position: ({x:.2f}, {y:.2f}, {z:.2f})"
            )
            
            node_sizes.append(max(5, freq * 3))
            # Color by centrality (blue = low, red = high)
            node_colors.append(centrality)
        
        node_trace = go.Scatter3d(
            x=node_x, y=node_y, z=node_z,
            mode='markers+text',
            hoverinfo='text',
            text=node_text,
            hovertext=node_info,
            textposition="middle center",
            textfont=dict(size=8),
            marker=dict(
                size=node_sizes,
                color=node_colors,
                colorscale='Viridis',
                colorbar=dict(
                    title="Centrality",
                    tickmode="linear",
                    tick0=0,
                    dtick=0.1
                ),
                line=dict(width=1, color='darkblue'),
                opacity=0.8
            ),
            name='Concepts'
        )
        
        # Create 3D figure
        fig = go.Figure(data=[edge_trace, node_trace])
        
        fig.update_layout(
            title=dict(
                text='Category Theory Knowledge Graph - 3D View',
                font=dict(size=16),
                x=0.5
            ),
            showlegend=True,
            hovermode='closest',
            margin=dict(b=20, l=5, r=5, t=40),
            scene=dict(
                xaxis=dict(showgrid=True, zeroline=False, showticklabels=False, title=''),
                yaxis=dict(showgrid=True, zeroline=False, showticklabels=False, title=''),
                zaxis=dict(showgrid=True, zeroline=False, showticklabels=False, title='Centrality'),
                bgcolor='white',
                camera=dict(
                    eye=dict(x=1.5, y=1.5, z=1.5)
                )
            ),
            annotations=[
                dict(
                    text="Drag to rotate • Scroll to zoom • Hover for details",
                    showarrow=False,
                    xref="paper", yref="paper",
                    x=0.005, y=0.005,
                    xanchor='left', yanchor='bottom',
                    font=dict(color='gray', size=10)
                )
            ]
        )
        
        output_path = self.output_path / output_file
        fig.write_html(str(output_path))
        
        print(f"3D visualization saved to: {output_path}")
    
    def export_data(self):
        """Export graph data in various formats"""
        # Export as GraphML (for Gephi, Cytoscape)
        nx.write_graphml(self.graph, self.output_path / "knowledge_graph.graphml")
        
        # Export as JSON for web applications
        graph_data = nx.node_link_data(self.graph)
        with open(self.output_path / "knowledge_graph.json", 'w') as f:
            json.dump(graph_data, f, indent=2)
        
        # Export concept frequency data
        with open(self.output_path / "concept_frequency.json", 'w') as f:
            json.dump(dict(self.concept_frequency), f, indent=2)
        
        # Export document-concept mapping
        doc_concepts_serializable = {doc: list(concepts) for doc, concepts in self.document_concepts.items()}
        with open(self.output_path / "document_concepts.json", 'w') as f:
            json.dump(doc_concepts_serializable, f, indent=2)
        
        print("Graph data exported in multiple formats")
    
    def generate_report(self):
        """Generate a comprehensive analysis report"""
        analysis = self.analyze_graph()
        
        report = f"""
# Category Theory Knowledge Graph Analysis Report

## Overview
- **Documents processed**: {len(self.document_concepts)}
- **Unique concepts**: {len(self.concept_frequency)}
- **Graph nodes**: {analysis.get('nodes', 0)}
- **Graph edges**: {analysis.get('edges', 0)}
- **Graph density**: {analysis.get('density', 0):.3f}

## Top Concepts by Centrality
"""
        
        if 'top_concepts' in analysis:
            for i, (concept, centrality) in enumerate(analysis['top_concepts'], 1):
                freq = self.concept_frequency.get(concept, 0)
                report += f"{i}. **{concept}** (centrality: {centrality:.3f}, frequency: {freq})\n"
        
        report += f"""

## Document-Concept Distribution
"""
        
        for doc, concepts in list(self.document_concepts.items())[:10]:  # Top 10 documents
            report += f"- **{doc}**: {len(concepts)} concepts\n"
        
        report += f"""

## Graph Statistics
- **Communities detected**: {analysis.get('communities', 0)}
- **Average degree**: {2 * analysis.get('edges', 0) / max(analysis.get('nodes', 1), 1):.2f}

## Files Generated
- `knowledge_graph.html` - Interactive visualization
- `knowledge_graph.png` - Static visualization  
- `knowledge_graph.graphml` - Graph data for Gephi/Cytoscape
- `knowledge_graph.json` - Graph data in JSON format
- `concept_frequency.json` - Concept frequency data
- `document_concepts.json` - Document-concept mappings
"""
        
        with open(self.output_path / "analysis_report.md", 'w') as f:
            f.write(report)
        
        print("Analysis report generated")
        return report

    def run_full_pipeline(self, min_frequency: int = 2, min_cooccurrence: int = 1):
        """Run the complete knowledge graph generation pipeline"""
        print("Starting Category Theory Knowledge Graph Generation...")
        print(f"Processing documents from: {self.docs_path}")
        
        # Process all markdown files
        markdown_files = list(self.docs_path.glob("**/*.md"))
        
        if not markdown_files:
            print("No markdown files found!")
            return
        
        print(f"Found {len(markdown_files)} markdown files")
        
        # Process each document
        results = []
        for file_path in markdown_files:
            try:
                result = self.process_document(file_path)
                results.append(result)
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
        
        # Build knowledge graph
        self.build_graph(min_frequency=min_frequency, min_cooccurrence=min_cooccurrence)
        
        # Generate visualizations and exports
        if self.graph.number_of_nodes() > 0:
            self.visualize_static()
            self.visualize_interactive()
            self.visualize_3d()
            self.export_data()
            report = self.generate_report()
            
            print("\n" + "="*50)
            print("KNOWLEDGE GRAPH GENERATION COMPLETE")
            print("="*50)
            print(f"Output directory: {self.output_path}")
            print("\nFiles generated:")
            print("- knowledge_graph.html (interactive 2D visualization)")
            print("- knowledge_graph_3d.html (interactive 3D visualization)")
            print("- knowledge_graph.png (static visualization)")
            print("- knowledge_graph.graphml (graph data)")
            print("- analysis_report.md (detailed analysis)")
            print("\nOpen knowledge_graph_3d.html in your browser for 3D exploration!")
            
        else:
            print("No graph generated - try lowering min_frequency parameter")


def main():
    parser = argparse.ArgumentParser(description='Generate knowledge graph from category theory documents')
    parser.add_argument('docs_path', help='Path to documents directory')
    parser.add_argument('--output', '-o', default='knowledge-graph', help='Output directory')
    parser.add_argument('--min-frequency', '-f', type=int, default=2, help='Minimum concept frequency')
    parser.add_argument('--min-cooccurrence', '-c', type=int, default=1, help='Minimum concept co-occurrence')
    
    args = parser.parse_args()
    
    # Create knowledge graph generator
    kg = CategoryTheoryKG(args.docs_path, args.output)
    
    # Run the complete pipeline
    kg.run_full_pipeline(
        min_frequency=args.min_frequency,
        min_cooccurrence=args.min_cooccurrence
    )


if __name__ == "__main__":
    main()
