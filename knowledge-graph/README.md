# Category Theory Knowledge Graph Generator

Automatically generate interactive knowledge graphs from your category theory markdown documents using spaCy NLP and NetworkX.

## Quick Start

1. **Setup** (one-time):
   ```bash
   cd knowledge-graph
   ./setup.sh
   ```

2. **Generate knowledge graph**:
   ```bash
   python3 kg_generator.py ../docs
   ```

3. **View results**: Open `knowledge-graph/knowledge_graph.html` in your browser

## What It Does

- **Extracts concepts** from markdown files using NLP
- **Identifies relationships** through co-occurrence analysis  
- **Recognizes category theory terms**: functors, monads, morphisms, etc.
- **Parses markdown links** like `[[concept]]` 
- **Generates visualizations**: interactive HTML + static PNG
- **Exports data**: GraphML for Gephi, JSON for web apps

## Output Files

- `knowledge_graph.html` - Interactive visualization (open in browser)
- `knowledge_graph.png` - Static image
- `knowledge_graph.graphml` - Import into Gephi/Cytoscape
- `analysis_report.md` - Detailed analysis
- `concept_frequency.json` - Term frequency data
- `document_concepts.json` - Document-concept mappings

## Options

```bash
# Basic usage
python3 kg_generator.py ../docs

# Custom output directory
python3 kg_generator.py ../docs --output my-knowledge-graph

# Filter rare concepts (appear less than 3 times)
python3 kg_generator.py ../docs --min-frequency 3

# Require stronger co-occurrence (appear together 2+ times)
python3 kg_generator.py ../docs --min-cooccurrence 2
```

## Features

- **Domain-aware**: Recognizes 50+ category theory terms
- **Multi-format**: Extracts from headers, links, code blocks
- **Customizable**: Adjust frequency and co-occurrence thresholds
- **Visual**: Node size = concept frequency, edge width = relationship strength
- **Exportable**: Multiple formats for further analysis

## Requirements

- Python 3.7+
- Internet connection (for initial spaCy model download)

The setup script handles all dependencies automatically.
