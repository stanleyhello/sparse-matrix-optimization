"""
Sparse Matrix using HashMap
"""

from sparse_linkedlist import *
from hashmap import *


class SparseMatrixNew:
    def __init__(self, nrows, ncols, default_value):
        self._validate_num_rows_cols(nrows, ncols)
        self._nrows = nrows
        self._ncols = ncols
        self._default_value = default_value
        self.rows_list = [HashMap() for _ in range(self._nrows)]
        self.clear()

    @property
    def nrows(self):
        return self._nrows

    @property
    def ncols(self):
        return self._ncols

    def clear(self):
        self.rows_list = [HashMap() for _ in range(self._nrows)]

    def _validate_num_rows_cols(self, nrows, ncols):
        if not isinstance(nrows, int):
            raise TypeError("number of rows should be int")
        if not isinstance(ncols, int):
            raise TypeError("number of columns should be int")
        if nrows <= 0:
            raise IndexError("number of rows and columns must be positive")
        if ncols <= 0:
            raise IndexError("number of rows and columns must be positive")

    def _validate_row_index(self, index):
        if not isinstance(index, int):
            raise TypeError("row index should be int")

        if index < 0 or index >= self._nrows:
            raise IndexError(f"row index {index} is invalid")

    def _validate_col_index(self, index):
        if not isinstance(index, int):
            raise TypeError("column index should be int")

        if index < 0 or index >= self._ncols:
            raise IndexError(f"column index {index} is invalid")

    def get(self, row_index, col_index):
        self._validate_row_index(row_index)
        self._validate_col_index(col_index)
        # row is a hashmap
        row = self.rows_list[row_index]
        try:
            return row[col_index]
        except KeyError:
            return self._default_value



    def set(self, row_index, col_index, new_value):
        self._validate_row_index(row_index)
        self._validate_col_index(col_index)
        # row is a hashmap
        if new_value == self._default_value:
            return
        row = self.rows_list[row_index]
        row[col_index] = new_value

    def get_row(self, row_index):
        self._validate_row_index(row_index)
        row = self.rows_list[row_index]
        for index in range(self._ncols):
            try:
                yield row[index]
            except KeyError:
                yield self._default_value


    def get_col(self, col):
        self._validate_col_index(col)

        def col_generator():
            index = 0
            while index < self._nrows:
                yield self.get(index, col)
                index += 1

        return col_generator()

    def _get_row_dict(self, row):
        return self.rows_list[row]

    def __str__(self):
        rows = []
        for i in range(self._nrows):
            row_values = [str(o) for o in self.get_row(i)]
            rows.append("  ".join(row_values))
        return "\n".join(rows)


class SparseMatrixMul(SparseMatrixNew):
    def __init__(self, nrows, ncols):
        super().__init__(nrows, ncols, 0)

    def __matmul__(self, other):

        if self.ncols != other.nrows:
            raise ValueError("Undefined product")

        result = SparseMatrixNew(self.nrows, other.ncols, 0)

        for i in range(self.nrows):
            # row is a hashmap
            row_dict = self._get_row_dict(i)
            for key in row_dict:
                for j in range(other.ncols):
                    result.set(i, j, result.get(i, j) + row_dict[key] * other.get(key, j))
        return result


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
