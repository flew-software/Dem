from typing import List, Tuple


def GetRow(l: List, rowIndex: int) -> List:
    """ gets a List and rowIndex and returns the row as a 1D list"""

    a = l[rowIndex]
    return a


def GetColoum(l: List, coloumIndex: int) -> List:
    """ gets a List and coloumIndex and returns the coloum as a 1D list"""

    out = []

    i = 0
    while i < len(l):
        out.append(GetRow(l, i)[coloumIndex])
        i += 1

    return out


def Replace(l: List, old: any, new: any) -> Tuple[List, int]:
    """ replaces the old value with the new value in the given list and returns the 2d list and change counter in a tuple """

    changeCounter = 0

    i = 0
    while i < len(l):
        ii = 0
        while ii < len(l[i]):
            if l[i][ii] == old:
                l[i][ii] = new
                changeCounter += 1
            ii += 1
        i += 1
    return (l, changeCounter)


def Find(l: List, val: any) -> List:
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
