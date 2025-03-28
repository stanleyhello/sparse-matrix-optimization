"""
CS3C, Assignment 2 Test
Stanley He
"""
import unittest
from sparse_matrix import *


class SparseMatrixTestCase(unittest.TestCase):

    # Get default value from a cell that's never set
    def testDefault(self):
        matrix = SparseMatrix(2, 2, 0)
        self.assertEqual(matrix._default_value, matrix.get(0, 0))
        self.assertEqual(matrix._default_value, matrix.get(0, 1))
        self.assertEqual(matrix._default_value, matrix.get(1, 0))
        self.assertEqual(matrix._default_value, matrix.get(1, 1))

    # Set a value at a row/column, and get the same value back; set it again to a
    # different value and get it back
    def testSet(self):
        matrix = SparseMatrix(2, 2, 0)
        matrix.set(0, 0, 5)
        self.assertEqual(5, matrix.get(0, 0))
        matrix.set(0, 0, 12)
        self.assertEqual(12, matrix.get(0, 0))

    # Set value at multiple columns of the same row, and get them back and verify
    def testSetInSameRow(self):
        matrix = SparseMatrix(5, 5, 0)
        matrix.set(2, 3, 30)
        matrix.set(2, 2, 20)
        matrix.set(2, 4, 40)
        self.assertEqual(30, matrix.get(2, 3))
        self.assertEqual(20, matrix.get(2, 2))
        self.assertEqual(40, matrix.get(2, 4))

    # Get a value from an invalid row/column, IndexError should be raised
    def testGetFailure(self):
        matrix = SparseMatrix(2, 2, 0)
        with self.assertRaises(IndexError):
            matrix.get(3, 3)
        with self.assertRaises(TypeError):
            matrix.get(1, "a")

    # Set a value at an invalid row/column, IndexError should be raised
    def testSetFailure(self):
        matrix = SparseMatrix(2, 2, 0)
        with self.assertRaises(IndexError):
            matrix.set(4, 4, 1)
        with self.assertRaises(TypeError):
            matrix.set(1, "a", 10)

    # Test get_row()/get_col(), make sure they raise IndexError for invalid input immediately
    def testGetRowFailure(self):
        matrix = SparseMatrix(2, 2, 0)
        with self.assertRaises(IndexError):
            matrix.get_row(3)
        with self.assertRaises(TypeError):
            matrix.get_row("a")
        with self.assertRaises(IndexError):
            matrix.get_col(3)
        with self.assertRaises(TypeError):
            matrix.get_col("a")

    # Test get_row()/get_col(), make sure they return a generator that yields the right values
    # for row/col
    def testGetRow(self):
        matrix = SparseMatrix(3, 3, 0)
        matrix.set(0, 2, 20)
        # matrix.set(0, 1, 10)
        matrix.set(0, 0, 1)
        expected = [1, 10, 20]
        actual = [o for o in matrix.get_row(0)]
        # self.assertEqual(expected, actual)
        print(actual)

    def testGetCol(self):
        matrix = SparseMatrix(3, 3, 0)
        matrix.set(0, 1, 1)
        matrix.set(1, 1, 10)
        matrix.set(2, 1, 20)
        expected = [1, 10, 20]
        actual = [o for o in matrix.get_col(1)]
        self.assertEqual(expected, actual)

    # Test __str__(); for this you can simply print out the retured str to inspect
    # (it's ok to write a testStr() method without using any self.assert*() in it),
    # or you can compose an expected str
    def testStr(self):
        matrix = SparseMatrix(3, 3, 0)
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

    def testClear(self):
        matrix = SparseMatrix(5, 5, 0)
        matrix.set(0, 0, 1)
        matrix.set(3, 3, 99)
        matrix.set(1, 4, 21)
        self.assertEqual(1, matrix.get(0, 0))
        self.assertEqual(99, matrix.get(3, 3))
        self.assertEqual(21, matrix.get(1, 4))
        matrix.clear()
        self.assertEqual(0, matrix.get(0, 0))
        self.assertEqual(0, matrix.get(3, 3))
        self.assertEqual(0, matrix.get(1, 4))

    def testSetDefault(self):
        matrix = SparseMatrix(4, 4, 0)
        matrix.set(0, 0, 1)
        matrix.set(0, 3, 3)
        matrix.set(0, 2, 2)
        matrix.set(0, 2, 0)
        row_one = matrix.rows_list[0]
        row_output = [cell.value for cell in row_one]
        expected = [1, 3]
        self.assertEqual(expected, row_output)
