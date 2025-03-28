"""
Test File for
Sparse Matrix with Python lists (sparse_list),
Sparse Matrix with my custom hash maps (sparse_hash),
Sparse Matrix with Python dicts (sparse_dict).
Uncomment the import that you want to test!
"""

# from sparse_list import *
from sparse_hash import *
# from sparse_dict import *

import unittest

DENSITY = 0.01

class SparseMatrixNewTestCase(unittest.TestCase):
    def testSet(self):
        matrix = SparseMatrixNew(2, 2, 0)
        matrix.set(0, 0, 5)
        self.assertEqual(5, matrix.get(0, 0))
        matrix.set(0, 0, 12)
        self.assertEqual(12, matrix.get(0, 0))

    def testGetRow(self):
        matrix = SparseMatrixNew(3, 3, 0)
        matrix.set(0, 2, 20)
        matrix.set(0, 1, 10)
        matrix.set(0, 0, 1)
        expected = [1, 10, 20]
        actual = [o for o in matrix.get_row(0)]
        self.assertEqual(expected, actual)
        print(actual)

        # Set value at multiple columns of the same row, and get them back and verify

    def testSetInSameRow(self):
        matrix = SparseMatrixNew(5, 5, 0)
        matrix.set(2, 3, 30)
        matrix.set(2, 2, 20)
        matrix.set(2, 4, 40)
        self.assertEqual(30, matrix.get(2, 3))
        self.assertEqual(20, matrix.get(2, 2))
        self.assertEqual(40, matrix.get(2, 4))

        # Get a value from an invalid row/column, IndexError should be raised

    def testGetFailure(self):
        matrix = SparseMatrixNew(2, 2, 0)
        with self.assertRaises(IndexError):
            matrix.get(3, 3)
        with self.assertRaises(TypeError):
            matrix.get(1, "a")

        # Set a value at an invalid row/column, IndexError should be raised

    def testSetFailure(self):
        matrix = SparseMatrixNew(2, 2, 0)
        with self.assertRaises(IndexError):
            matrix.set(4, 4, 1)
        with self.assertRaises(TypeError):
            matrix.set(1, "a", 10)

        # Test get_row()/get_col(), make sure they raise IndexError for invalid input immediately

    def testGetRowFailure(self):
        matrix = SparseMatrixNew(2, 2, 0)
        with self.assertRaises(IndexError):
            matrix.get_row(3)
        with self.assertRaises(TypeError):
            matrix.get_row("a")
        with self.assertRaises(IndexError):
            matrix.get_col(3)
        with self.assertRaises(TypeError):
            matrix.get_col("a")

    def testStr(self):
        matrix = SparseMatrixNew(3, 3, 0)
        matrix.set(0, 0, 1)
        matrix.set(1, 0, 2)
        matrix.set(2, 0, 3)
        matrix.set(0, 1, 4)
        matrix.set(1, 1, 5)
        matrix.set(2, 1, 6)
        matrix.set(0, 2, 7)
        matrix.set(1, 2, 8)
        matrix.set(2, 2, 9)
        print(matrix)

