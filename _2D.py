from typing import List, Tuple


def get_row(l: List, row_index: int) -> List:
    """ gets a List and rowIndex and returns the row as a 1D list"""

    a = l[row_index]
    return a


def get_column(l: List, column_index: int) -> List:
    """ gets a List and columnIndex and returns the column as a 1D list"""

    out = []

    i = 0
    while i < len(l):
        out.append(get_row(l, i)[column_index])
        i += 1

    return out


def replace(l: List, old: any, new: any) -> Tuple[List, int]:
    """
    replaces the old value with the new value in the given list and returns the 2d list and change counter in a
    tuple
    """

    change_counter = 0

    i = 0
    while i < len(l):
        ii = 0
        while ii < len(l[i]):
            if l[i][ii] == old:
                l[i][ii] = new
                change_counter += 1
            ii += 1
        i += 1
    return l, change_counter


def find(l: List, val: any) -> List:
    """ find the val in list and returns a list containing a list(s) with row and coloum of the location of the value"""

    out = []

    i = 0  # row
    while i < len(l):
        ii = 0
        while ii < len(l[i]):
            if l[i][ii] == val:
                out.append([i, ii])
            ii += 1
        i += 1
    return out
