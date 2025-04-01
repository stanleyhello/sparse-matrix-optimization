import importlib
import unittest
import numpy as np
import scipy.sparse
import time
import sys

DENSITY = 0.01

import importlib
import sys

def choose_module():
    print("Let's test performance of various sparse matrices!")
    print(f"Currently testing at {DENSITY * 100}% matrix density.")
    print("Choose which sparse matrix implementation to test:")
    print("1: Sparse Matrix with linked lists")
    print("2: Sparse Matrix with Python lists")
    print("3: Sparse Matrix with hash maps")
    print("4: Sparse Matrix with Python dicts")
    choice = input("Enter your choice (1-4): ").strip()

    module_mapping = {
        "1": "sparse_linkedlist",
        "2": "sparse_list",
        "3": "sparse_hash",
        "4": "sparse_dict"
    }

    description_mapping = {
        "1": "Sparse Matrix with linked lists",
        "2": "Sparse Matrix with Python lists",
        "3": "Sparse Matrix with hash maps",
        "4": "Sparse Matrix with Python dicts"
    }

    if choice in module_mapping:
        print(f"You selected: {description_mapping[choice]}")
        return importlib.import_module(module_mapping[choice])
    else:
        print("Invalid choice. Exiting.")
        sys.exit(1)

# Dynamically import the selected module.
sparse_module = choose_module()

# Assign the necessary classes and functions from the imported module.
SparseMatrixMul = sparse_module.SparseMatrixMul
SparseMatrixNew = sparse_module.SparseMatrixNew
mulmat = sparse_module.mulmat


# Define test cases using unittest.
class SparseMatrixTestCase(unittest.TestCase):
    def print_header(self, title):
        print(f"\n{'=' * 60}")
        print(f"{title:^60}")
        print(f"{'=' * 60}")
        print(f"{'Matrix Size':<20}{'Time (seconds)':<20}")
        print(f"{'-' * 60}")

    def generate_random_matrices(self, n):
        a = scipy.sparse.random(n, n, density=DENSITY, dtype=np.uint8).toarray().tolist()
        b = scipy.sparse.random(n, n, density=DENSITY, dtype=np.uint8).toarray().tolist()
        return a, b

    def testPerformanceSparseMatMul(self):
        self.print_header("SparseMatrixMul.__matmul__ Performance")
        for n in list(range(10, 100, 10)) + list(range(100, 600, 100)):
            a_list, b_list = self.generate_random_matrices(n)

            A = SparseMatrixMul(n, n)
            B = SparseMatrixNew(n, n, 0)
            for i in range(n):
                for j in range(n):
                    A.set(i, j, a_list[i][j])
                    B.set(i, j, b_list[i][j])

            start = time.perf_counter()
            _ = A @ B
            duration = time.perf_counter() - start
            print(f"{n:<20}{duration:.08f}")

    def testPerformanceMulMat(self):
        self.print_header("mulmat() Function Performance")
        for n in list(range(10, 100, 10)) + list(range(100, 600, 100)):
            a_list, b_list = self.generate_random_matrices(n)

            start = time.perf_counter()
            _ = mulmat(a_list, b_list)
            duration = time.perf_counter() - start
            print(f"{n:<20}{duration:.08f}")

    def testPerformanceNumpy(self):
        self.print_header("NumPy matmul Performance")
        for n in list(range(10, 100, 10)) + list(range(100, 600, 100)):
            a = scipy.sparse.random(n, n, density=DENSITY, dtype=np.uint8).toarray()
            b = scipy.sparse.random(n, n, density=DENSITY, dtype=np.uint8).toarray()

            start = time.perf_counter()
            _ = np.matmul(a, b)
            duration = time.perf_counter() - start
            print(f"{n:<20}{duration:.08f}")


    def testSquareMatrices(self):
        a = [
            [3, 0],
            [2, 6]
        ]
        b = [
            [7, 2],
            [0, 2]
        ]
        A = SparseMatrixMul(2, 2)
        A.set(0, 0, 3)
        A.set(1, 0, 2)
        A.set(1, 1, 6)
        B = SparseMatrixNew(2, 2, 0)
        B.set(0, 0, 7)
        B.set(0, 1, 2)
        B.set(1, 1, 2)
        normal_result = mulmat(a, b)
        product = A.__matmul__(B)
        sparse_result = [list(product.get_row(i)) for i in range(product.nrows)]
        self.assertEqual(normal_result, sparse_result)

    def testRectangularMatrices(self):
        a = [
            [6, 6, 8],
            [1, 0, 5]
        ]
        b = [
            [9, 4],
            [2, 2],
            [0, 1]
        ]
        A = SparseMatrixMul(2, 3)
        A.set(0, 0, 6)
        A.set(0, 1, 6)
        A.set(0, 2, 8)
        A.set(1, 0, 1)
        A.set(1, 2, 5)
        B = SparseMatrixNew(3, 2, 0)
        B.set(0, 0, 9)
        B.set(0, 1, 4)
        B.set(1, 0, 2)
        B.set(1, 1, 2)
        B.set(2, 1, 1)
        normal_result = mulmat(a, b)
        product = A.__matmul__(B)
        sparse_result = [list(product.get_row(i)) for i in range(product.nrows)]
        self.assertEqual(normal_result, sparse_result)

    def testLargeMatrices(self):
        sm_numpy_a = scipy.sparse.random(10, 10, density=0.1, dtype=np.uint8).toarray().tolist()

        A = SparseMatrixMul(10, 10)
        for i in range(len(sm_numpy_a)):
            for j in range(len(sm_numpy_a[0])):
                A.set(i, j, sm_numpy_a[i][j])

        sm_numpy_b = scipy.sparse.random(10, 10, density=0.1, dtype=np.uint8).toarray().tolist()

        B = SparseMatrixNew(10, 10, 0)
        for i in range(len(sm_numpy_b)):
            for j in range(len(sm_numpy_b[0])):
                B.set(i, j, sm_numpy_b[i][j])

        mulmat_result = mulmat(sm_numpy_a, sm_numpy_b)
        product = A.__matmul__(B)
        sparse_result = [list(product.get_row(i)) for i in range(product.nrows)]
        sm_numpy_a_arr = np.array(sm_numpy_a)
        sm_numpy_b_arr = np.array(sm_numpy_b)
        numpy_result = np.matmul(sm_numpy_a_arr, sm_numpy_b_arr).tolist()

        self.assertEqual(numpy_result, mulmat_result)
        self.assertEqual(numpy_result, sparse_result)


def main():

    print("No tests are running automatically. To run tests, relaunch the file with '--run-tests'.")

if __name__ == "__main__":
    # Run the tests only if '--run-tests' is provided as a command-line argument.
    if "--run-tests" in sys.argv:
        sys.argv.remove("--run-tests")
        unittest.main()
    else:
        main()
