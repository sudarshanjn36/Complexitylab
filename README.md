📖 ComplexityLab Documentation
🧩 What is ComplexityLab?

ComplexityLab is a Python package designed to analyze algorithms in practice.
It measures how runtime and memory usage change as input sizes grow, and then compares these results against standard Big-O complexity classes (O(1), O(log n), O(n), O(n log n), O(n²), etc.).

The goal is to bridge the gap between theoretical complexity (what we learn in textbooks) and real-world performance (what happens when code runs on a machine).

📌 Features

Analyze time complexity empirically by running functions on multiple input sizes.

Track memory consumption to study space complexity.

Compare results with known growth curves (constant, log, linear, quadratic, cubic, exponential).

Generate a report that clearly shows the best-fit complexity class.

Provide both a Python API and a command-line interface (CLI).

📂 Project Structure (Theory)

The package follows a professional, industry-style layout:

pyproject.toml → Configuration file that tells Python how to build and install the package.

README.md → Documentation file (you are reading a detailed version of it here).

src/complexitylab/ → Main source code folder, containing:

analyzer.py → Responsible for measuring runtime and memory.

fitting.py → Fits measured results to theoretical Big-O functions.

report.py → Formats the output into readable tables and summaries.

cli.py → Allows running the tool directly from the terminal.

examples/ → Example algorithms (like Bubble Sort) to test the package.

⚙️ How Does It Work? (Step by Step)

Measure Runtime & Memory

Run an algorithm on inputs of size n = 100, 200, 400, etc.

Record how long it takes and how much memory it uses.

Generate Candidate Curves

Standard functions are used as models:

O(1): constant

O(log n): logarithmic

O(n): linear

O(n log n): linearithmic

O(n²): quadratic

O(n³): cubic

O(2ⁿ): exponential

Fit Curves to Data

The package compares the measured runtimes against these functions.

Each curve is scaled to match the data (so units like “seconds” don’t matter).

An error score is computed — the smaller the error, the better the fit.

Pick Best Fit

The curve with the lowest error is chosen as the predicted complexity class.

Example: Bubble Sort produces results that closely match O(n²).

Report Results

A table shows runtime and memory usage.

A summary highlights the best-fit complexity and error scores for all candidates.

🖥️ Usage Modes
1. Python API (inside your scripts)

You can import the package, pass in your function and input generator, and get results.
Example workflow:

Define an algorithm (e.g., Bubble Sort).

Define an input generator (e.g., reversed list of size n).

Call the analyzer with input sizes.

Print results and complexity fit.

2. Command Line Interface (CLI)

You can run the analysis directly from the terminal.

--func specifies which algorithm to analyze.

--gen specifies how to generate inputs.

--sizes provides a list of input sizes.

This makes it possible to test algorithms quickly without writing extra Python scripts.

📊 Example Output (Interpreted)

When analyzing Bubble Sort, you may see something like:

n       time(s)     mem(bytes)
100     0.0009      944
200     0.0033      1744
400     0.0485      3468
800     0.1912      7000

Complexity Fit Results:
Best Fit: O(n^2) (error=1.45e-06)

All Fits (sorted):
O(n^2)     error=1.45e-06
O(n log n) error=2.31e-05
O(n)       error=1.23e-04
O(log n)   error=1.22e-03
O(1)       error=1.44e-03


Interpretation:

The runtime clearly grows quadratically (doubling input makes time roughly 4x).

Memory also grows with input size, but complexity analysis focuses mainly on runtime.

📖 Roadmap (Future Improvements)

Add confidence scores for predictions (e.g., 95% chance it’s O(n²)).

Extend to space complexity fitting (not just time).

Add support for exporting results (--json-out results.json).

Generate plots of runtime curves.

Include more algorithm examples and automated tests.