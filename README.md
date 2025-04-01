# Sparse Matrix Speed Optimization Project

This project compares different sparse matrix implementations in Python. It includes performance benchmarking and correctness testing for:

-  Linked List–based sparse matrix
-  List of lists (Python-native lists)
-  Custom hash map–based sparse matrix
-  Python built-in `dict`–based sparse matrix
  
https://www.youtube.com/watch?v=VbN12C21xuc

##  How to Run the Tests

The performance and correctness tests are interactive and run via the terminal.

### 🔧 Requirements
- Python 3.8+
- NumPy
- SciPy
### 1. Install Python dependencies
Make sure you have Python installed (Python 3.8+ recommended).
Install the required libraries:
```bash
pip install numpy scipy
```
### 2. Run the test script
In your terminal (inside this project folder), run:
```bash
python performance_tests.py --run-tests
```
### 3. Choose which version to test
When prompted, type a number to choose the sparse matrix version:
```bash
Choose which sparse matrix implementation to test:
1: Sparse Matrix with linked lists
2: Sparse Matrix with Python lists
3: Sparse Matrix with hash maps
4: Sparse Matrix with Python dicts
Enter your choice (1-4):

```

## Project Structure

| File                  | Description |
|-----------------------|-------------|
| `sparse_linkedlist.py` | Sparse matrix using ordered linked lists (used in performance tests) |
| `sparse_list.py`       | Sparse matrix using Python lists |
| `sparse_hash.py`       | Sparse matrix using a custom hash map |
| `sparse_dict.py`       | Sparse matrix using Python `dict` |
| `sparse_matrix.py`     | (Original version, linked list–based, no multiplication) |
| `performance_tests.py` | Main test script for correctness and benchmarking |
| `basic_tests.py`       | Simpler test file for development or small tests |
| `linkedlist.py`        | Linked list implementation used in `sparse_linkedlist.py` |
| `hashmap.py`, `hashqp.py` | Hash map implementation used in `sparse_hash.py` |
| `README.md`           | You're reading it! |


## What’s Being Tested?
Each test case checks:

- Matrix multiplication correctness (A @ B)

- Performance of custom sparse matrix multiplication vs:

 A pure Python mulmat() fallback function

NumPy's matmul on dense equivalents

Matrix sizes scale from 10x10 to 500x500 with 1% density, using scipy.sparse.random().


## Example Output

```bash
Let's test performance of various sparse matrices!
Currently testing at 1.0% matrix density.
Choose which sparse matrix implementation to test:
1: Sparse Matrix with linked lists
2: Sparse Matrix with Python lists
3: Sparse Matrix with hash maps
4: Sparse Matrix with Python dicts
Enter your choice (1-4): You selected: Sparse Matrix with linked lists
============================================================
           SparseMatrixMul.__matmul__ Performance           
============================================================
Matrix Size         Time (seconds)      
------------------------------------------------------------
10                  0.00001230
20                  0.00016810
30                  0.00054450
40                  0.00144650
50                  0.00273740
60                  0.00537860
70                  0.00882730
80                  0.01304480
90                  0.02060060
100                 0.02837570
200                 0.33072140
300                 1.54080580
400                 4.81001310
500                 11.64873780
```
Note: Output values may vary depending on your machine.

## Recommended Setup
To keep things clean, use a Python virtual environment:

```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
```
# On Mac/Linux:
```bash
source .venv/bin/activate
```
Then install any required packages (if applicable).

## About
Created by Stanley He

GitHub: @stanleyhello