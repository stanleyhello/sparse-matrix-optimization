# Sparse Matrix Speed Optimization Project

This project explores and benchmarks various data structures for sparse matrix representation and other algorithmic operations in Python. It includes implementations of hashmaps, linked lists, sparse matrices, and performance tests.
https://www.youtube.com/watch?v=VbN12C21xuc
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
├── README.md                      # Project overview and instructions
├── .gitignore                     # Git rules for ignored files/folders
├── performance_tests.py          # Benchmarking entry point
├── basic_tests.py                # General validation tests

├── Data Structures/
│   ├── hashmap.py                # Custom hashmap implementation
│   ├── hashqp.py                 # Hashing with quadratic probing
│   ├── linkedlist.py             # Singly linked list implementation
│   ├── prime.py                  # Prime number utils (for hashing)
│   ├── sparse_dict.py           # Sparse matrix using dictionary
│   ├── sparse_hash.py           # Sparse matrix using hash table
│   ├── sparse_matrix.py     # Sparse matrix using linked list
│   ├── sparse_list.py           # Sparse matrix using list

├── .venv/                        # Virtual environment (ignored)
├── __pycache__/                  # Python bytecode cache (ignored)
├── .idea/                        # IDE config (ignored)

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
