"""
Assignment 3 Testing
Stanley He
"""
import unittest
from matrix_multiplication import *
import numpy
import scipy
import time


class SparseMatrixMulTestCase(unittest.TestCase):
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
        B = SparseMatrix(2, 2, 0)
        B.set(0, 0, 7)
        B.set(0, 1, 2)
        B.set(1, 1, 2)

        normal_result = mulmat(a, b)
        product = A.__matmul__(B)
        sparse_result = []
        for i in range(product.nrows):
            row_lst = [o for o in product.get_row(i)]
            sparse_result.append(row_lst)

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

        B = SparseMatrix(3, 2, 0)
        B.set(0, 0, 9)
        B.set(0, 1, 4)
        B.set(1, 0, 2)
        B.set(1, 1, 2)
        B.set(2, 1, 1)

        normal_result = mulmat(a, b)
        product = A.__matmul__(B)
        sparse_result = []
        for i in range(product.nrows):
            row_lst = [o for o in product.get_row(i)]
            sparse_result.append(row_lst)

        self.assertEqual(normal_result, sparse_result)

    def testLargeMatrices(self):

        sm_numpy_a = scipy.sparse.random(10, 10, density=0.1, dtype=numpy.uint8).toarray()
        sm_numpy_a = sm_numpy_a.tolist()

        A = SparseMatrixMul(10, 10)
        for i in range(len(sm_numpy_a)):
            for j in range(len(sm_numpy_a[0])):
                A.set(i, j, sm_numpy_a[i][j])

        sm_numpy_b = scipy.sparse.random(10, 10, density=0.1, dtype=numpy.uint8).toarray()
        sm_numpy_b = sm_numpy_b.tolist()

        B = SparseMatrix(10, 10, 0)
        for i in range(len(sm_numpy_b)):
            for j in range(len(sm_numpy_b[0])):
                B.set(i, j, sm_numpy_b[i][j])

        mulmat_result = mulmat(sm_numpy_a, sm_numpy_b)

        product = A.__matmul__(B)
        sparse_result = []
        for i in range(product.nrows):
            row_lst = [o for o in product.get_row(i)]
            sparse_result.append(row_lst)

        sm_numpy_a = numpy.array(sm_numpy_a)
        sm_numpy_b = numpy.array(sm_numpy_b)
        numpy_result = numpy.matmul(sm_numpy_a, sm_numpy_b)
        numpy_result = numpy_result.tolist()

        self.assertEqual(numpy_result, mulmat_result)
        self.assertEqual(numpy_result, sparse_result)

    def testPerformanceMulMat(self):
        print("mulmat()")
        for n in range(10, 100, 10):
            sm_numpy_a = scipy.sparse.random(n, n, density=0.01, dtype=numpy.uint8).toarray()
            sm_numpy_a = sm_numpy_a.tolist()
            sm_numpy_b = scipy.sparse.random(n, n, density=0.001, dtype=numpy.uint8).toarray()
            sm_numpy_b = sm_numpy_b.tolist()

            start = time.perf_counter()
            mulmat(sm_numpy_a, sm_numpy_b)
            duration = time.perf_counter() - start
            print(f"size: {n} - time: {duration:.08f}")

        for n in range(100, 1000, 100):
            sm_numpy_a = scipy.sparse.random(n, n, density=0.01, dtype=numpy.uint8).toarray()
            sm_numpy_a = sm_numpy_a.tolist()
            sm_numpy_b = scipy.sparse.random(n, n, density=0.01, dtype=numpy.uint8).toarray()
            sm_numpy_b = sm_numpy_b.tolist()

            start = time.perf_counter()
            mulmat(sm_numpy_a, sm_numpy_b)
            duration = time.perf_counter() - start
            print(f"size: {n} - time: {duration:.08f}")

    def testPerformanceSparseMatMul(self):
        print("SparseMatrixMul.__matmul__")
        for n in range(10, 100, 10):
            sm_numpy_a = scipy.sparse.random(n, n, density=0.01, dtype=numpy.uint8).toarray()
            sm_numpy_a = sm_numpy_a.tolist()
            sm_numpy_b = scipy.sparse.random(n, n, density=0.01, dtype=numpy.uint8).toarray()
            sm_numpy_b = sm_numpy_b.tolist()

            A = SparseMatrixMul(n, n)
            for i in range(len(sm_numpy_a)):
                for j in range(len(sm_numpy_a[0])):
                    A.set(i, j, sm_numpy_a[i][j])
            B = SparseMatrix(n, n, 0)
            for i in range(len(sm_numpy_b)):
                for j in range(len(sm_numpy_b[0])):
                    B.set(i, j, sm_numpy_b[i][j])

            start = time.perf_counter()
            A.__matmul__(B)
            duration = time.perf_counter() - start
            print(f"size: {n} - time: {duration:.08f}")

        for n in range(100, 1000, 100):
            sm_numpy_a = scipy.sparse.random(n, n, density=0.01, dtype=numpy.uint8).toarray()
            sm_numpy_a = sm_numpy_a.tolist()
            sm_numpy_b = scipy.sparse.random(n, n, density=0.01, dtype=numpy.uint8).toarray()
            sm_numpy_b = sm_numpy_b.tolist()

            A = SparseMatrixMul(n, n)
            for i in range(len(sm_numpy_a)):
                for j in range(len(sm_numpy_a[0])):
                    A.set(i, j, sm_numpy_a[i][j])
            B = SparseMatrix(n, n, 0)
            for i in range(len(sm_numpy_b)):
                for j in range(len(sm_numpy_b[0])):
                    B.set(i, j, sm_numpy_b[i][j])

            start = time.perf_counter()
            A.__matmul__(B)
            duration = time.perf_counter() - start
            print(f"size: {n} - time: {duration:.08f}")

    def testPerformanceNumpy(self):
        print("numpy.matmul")
        for n in range(10, 100, 10):
            sm_numpy_a = scipy.sparse.random(n, n, density=0.001, dtype=numpy.uint8).toarray()
            sm_numpy_b = scipy.sparse.random(n, n, density=0.001, dtype=numpy.uint8).toarray()

            start = time.perf_counter()
            numpy_result = numpy.matmul(sm_numpy_a, sm_numpy_b)
            duration = time.perf_counter() - start
            print(f"size: {n} - time: {duration:.08f}")

        for n in range(100, 1000, 100):
            sm_numpy_a = scipy.sparse.random(n, n, density=0.001, dtype=numpy.uint8).toarray()
            sm_numpy_b = scipy.sparse.random(n, n, density=0.001, dtype=numpy.uint8).toarray()

            start = time.perf_counter()
            numpy_result = numpy.matmul(sm_numpy_a, sm_numpy_b)
            duration = time.perf_counter() - start
            print(f"size: {n} - time: {duration:.08f}")
