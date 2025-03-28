"""
Assignment 3: Timing Matrix Multiplication
Stanley He
I used my own implementation of SparseMatrix.
"""
from sparse_matrix import *


def mulmat(a, b):
    a_nrows = len(a)
    a_ncols = len(a[0])
    b_nrows = len(b)
    b_ncols = len(b[0])

    if a_ncols != b_nrows:
        raise ValueError("Undefined product")

    result = [[0 for _ in range(b_ncols)] for _ in range(a_nrows)]

    for i in range(a_nrows):
        for j in range(b_ncols):
            for k in range(b_nrows):
                result[i][j] += a[i][k] * b[k][j]

    return result


class SparseMatrixMul(SparseMatrix):
    def __init__(self, nrows, ncols):
        super().__init__(nrows, ncols, 0)

    def __matmul__(self, other):

        if self.ncols != other.nrows:
            raise ValueError("Undefined product")

        result = SparseMatrix(self.nrows, other.ncols, 0)

        for i in range(self.nrows):
            for cell in self._get_row_list(i):
                for j in range(other.ncols):
                    result.set(i, j, result.get(i, j) + cell.value * other.get(cell.column, j))
        return result


"""
Expectations:
I expect matmul() to run at O(n^3) since the number of rows in the b matrix, times the number of columns in the
b matrix, time the number of rows in the a matrix.
I expect SparseMatrixMul.__matmul__() to also run at O(n^3) because it also uses 3 nested loops. However, since in
the second loop it only has to iterate through the cells that have values in the row and can skip the default values,
it should be a bit faster. 

Actual:
My SparseMatrixMul.__matmul__() actually ran slower than matmul(). Numpy multiplication was super fast. I derived
performance times by using numpy to generate random sparse matrices which were 1% full and doing multiplication
with them for each of the 3 functions. I used the time module to measure time. My sparse matrix multiplication being
slower was definitely surprising. I think it is because inside the third nested loop, I call .get(), which itself
loop through the linked list. Maybe this makes the function have O(n^4). 
I graphed my results using google sheets:
https://docs.google.com/spreadsheets/d/1zONuFhb4eNnsWd_ai74tyeLbK4gY12ZjqnBuoxenCu0/edit?usp=sharing

Numpy was the fastest. matmul(), the function thaat just does matrix multipliction normally, going through every column
of each row, was the second fastest. And my SparseMatrixMul.__mulmat__() was the slowest. I think this is because
I actually go through 4 loops, making it O(n^4) and also because it only takes advantage of the sparseness of the first
matrix. 
"""
