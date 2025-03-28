# Sparse Matrix Speed Optimization Project

This project explores and benchmarks various data structures for sparse matrix representation and other algorithmic operations in Python. It includes implementations of hashmaps, linked lists, sparse matrices, and performance tests.

## How to Run

Make sure you have **Python 3.8+** installed.

Clone this repo, then in the project directory run:

```bash
python performance_tests.py
```
This will run performance comparisons using the custom data structures implemented in this project.


## Project Structure
```bash
.
├── performance_tests.py               # Benchmarking entry point
├── sparse_matrix.py                   # Sparse matrix implementation
├── sparse_dict.py                     # Sparse representation using a dictionary
├── sparse_list.py                     # Sparse representation using a list
├── sparse_hash.py                     # Sparse representation using hashing
├── hashmap.py                         # Custom hashmap implementation
├── hashmap_solution.py                # Provided or reference hashmap solution
├── hashmap_test.py                    # Tests for hashmap
├── hashqp.py                          # Hashing with quadratic probing
├── hashqp_solution.py                 # Reference solution for hashqp
├── linkedlist.py                      # Singly linked list implementation
├── matrix_multiplication.py          # Matrix multiplication using custom structures
├── matrix_multiplication_test.py     # Tests for matrix multiplication
├── basic_tests.py                     # Basic validation tests
├── prime.py                           # Prime number utilities (likely for hashing)
├── sparse_matrix_test.py             # Tests for sparse matrix functionality
├── .idea/, __pycache__, .venv        # Auto-generated files (can be ignored)

```
## Testing
You can run the provided test scripts individually, for example:

```bash
python sparse_matrix_test.py
python hashmap_test.py
```
Each test script validates the functionality of its corresponding module.

## Example Output

```bash
Testing performance of different sparse matrix implementations...

SparseDict Lookup Time: 0.0023s
SparseList Lookup Time: 0.0079s
SparseHash Lookup Time: 0.0011s

All tests completed.
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
Created by Stanley

GitHub: @stanleyhello
