def row_major(l: list) -> tuple[list, int]:
    """ converts a 2d list to a 1d list using row major algorithm and returns a 1d list and row count """

    out = []
    i = 0
    while i < len(l):
        ii = 0
        a = l[i]
        while ii < len(a):
            out.append(a[ii])
            ii += 1
        i += 1

    return out, len(l)
