#!/bin/bash

# Setup script for Category Theory Knowledge Graph Generator

echo "Setting up Category Theory Knowledge Graph Generator..."

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is required but not installed."
    exit 1
fi

# Install requirements
echo "Installing Python dependencies..."
pip3 install -r requirements.txt

# Download spaCy English model
echo "Downloading spaCy English model..."
python3 -m spacy download en_core_web_sm

echo "Setup complete!"
echo ""
echo "Usage:"
echo "  python3 kg_generator.py ../docs"
echo "  python3 kg_generator.py ../docs --output my-graph --min-frequency 3"
echo ""
echo "This will process all markdown files in your docs folder and generate:"
echo "  - Interactive HTML visualization"
echo "  - Static PNG image"
echo "  - Graph data files (GraphML, JSON)"
echo "  - Analysis report"
