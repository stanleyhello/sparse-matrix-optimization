"""
CS3C, Assignment 2, Sparse Matrix
Stanley He
"""
from linkedlist import *


class MatrixEntry:
    def __init__(self, value, column):
        self._value = value
        self._column = column

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    @property
    def column(self):
        return self._column

    def __lt__(self, other):
        if isinstance(other, MatrixEntry):
            return self.column < other.column
        else:
            return self.column < other

    def __gt__(self, other):
        if isinstance(other, MatrixEntry):
            return self.column > other.column
        else:
            return self.column > other

    def __eq__(self, other):
        if isinstance(other, MatrixEntry):
            return self.column == other.column
        else:
            return self.column == other


class SparseMatrixNew:
    def __init__(self, nrows, ncols, default_value):
        self._validate_num_rows_cols(nrows, ncols)
        self._nrows = nrows
        self._ncols = ncols
        self._default_value = default_value
        self.rows_list = [OrderedLinkedList() for _ in range(self._nrows)]
        self.clear()

    @property
    def nrows(self):
        return self._nrows

    @property
    def ncols(self):
        return self._ncols

    def clear(self):
        self.rows_list = [OrderedLinkedList() for _ in range(self._nrows)]

    def _validate_num_rows_cols(self, nrows, ncols):
        if not isinstance(nrows, int):
            raise TypeError("number of rows should be int")
        if not isinstance(ncols, int):
            raise TypeError("number of columns should be int")
        if nrows <= 0 or ncols <= 0:
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

    def get(self, row, col):
        self._validate_row_index(row)
        self._validate_col_index(col)
        row_list = self.rows_list[row]
        try:
            return row_list.find(col).value
        except KeyError:
            return self._default_value

    def set(self, row, col, new_value):
        self._validate_row_index(row)
        self._validate_col_index(col)

        row_list = self.rows_list[row]

        try:
            cell = row_list.find(col)
            if new_value == self._default_value:
                row_list.remove(cell)
            else:
                cell.value = new_value
        except KeyError:
            if new_value != self._default_value:
                entry = MatrixEntry(new_value, col)
                row_list.add(entry)

    def get_row(self, row):
        self._validate_row_index(row)

        def row_generator():
            index = 0
            row_list = self.rows_list[row]
            curr = iter(row_list)
            next_cell = next(curr, None)
            while index < self._ncols:
                if next_cell is not None and next_cell.column == index:
                    yield next_cell.value
                    next_cell = next(curr, None)
                else:
                    yield self._default_value
                index += 1

        return row_generator()

    def get_col(self, col):
        self._validate_col_index(col)

        def col_generator():
            index = 0
            while index < self._nrows:
                yield self.get(index, col)
                index += 1

        return col_generator()

    def _get_row_list(self, row):
        return self.rows_list[row]

    def __str__(self):
        rows = []
        for i in range(self._nrows):
            row_values = [str(o) for o in self.get_row(i)]
            rows.append("  ".join(row_values))
        return "\n".join(rows)


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
