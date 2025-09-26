# ComplexityLab

**ComplexityLab** is a Python package for empirically analyzing **time** and **space complexity** of algorithms.  
It allows you to run an algorithm with different input sizes, measure runtime and peak memory usage, and collect results for further analysis.

---

## Features (Day 1)
- Run any function with generated input of different sizes.
- Measure **runtime** in seconds.
- Measure **peak memory usage** in bytes.
- Return results in a clean table (list of dictionaries).
- Organized as a Python package for easy extension.

---

## Project Structure
Complexitylab/
│ pyproject.toml ← Package configuration
│ README.md ← Documentation
│
├── src/
│ └── complexitylab/
│ ├── init.py ← Marks folder as a Python package
│ └── analyzer.py ← Core analyzer logic
│
└── examples/
└── sorting_example.py ← Example usage (Bubble Sort)
    
---

## ⚙️ Installation
From the root of the project, install in editable mode:

## pip install -e .( in the bash)
This makes the complexitylab package available for import while allowing you to keep editing the source code.
  Running the Example
  ## python examples/sorting_example.py
  