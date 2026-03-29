# MindMapper
MindMapper is a Python application that transforms raw text into a structured mind map by automatically extracting semantic relationships and visualizing them as a directed graph.

#Features

**Semantic Extraction**  
  Parses input text to identify subjects and relationships using predefined connectors  
  (e.g., "is", "used in", "such as", "pour", "dans", etc.)

**Graph Construction**  
  Builds a directed graph structure where:
  - Nodes represent concepts
  - Edges represent relationships between them

**Visualization**  
  Uses NetworkX and Matplotlib to render a dynamic mind map with labeled connections

**Graphical Interface**  
  Simple Tkinter-based UI allowing users to input text and generate mind maps instantly
  
**Technologies Used**
- Python
- NetworkX
- Matplotlib
- Tkinter

**How It Works**

1. The user inputs a sentence or paragraph in the interface
2. The text is analyzed to extract key relationships
3. A structured dictionary is generated
4. The graph builder converts it into a directed graph
5. The renderer displays the mind map visually

**Example**

Input:
Python is used in data science. Data science is used in AI.


Output:
A graph showing:
- Python → data science (used in)
- data science → AI (used in)

**Future Improvements**
- Better NLP (more advanced parsing instead of simple connectors)
- Interactive graph (zoom, drag, edit nodes)
- Export as image or PDF
- GUI improvements

**Goal**

This project is designed to explore:
- Graph theory applications
- Basic NLP techniques
- Data visualization
- GUI development in Python

**Author**
Developed as part of a personal learning and portfolio project.
