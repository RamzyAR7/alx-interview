#!/usr/bin/python3
''' 0-pascal_triangle.py '''


def pascal_triangle(n):

    '''
    Returns a list of lists of integers representing
    the Pascal’s triangle of n.
    '''

    if (n <= 0):
        return []

    triangle = [[1]]
    for r in range(1, n):
        prev = triangle[-1]
        new = [1]

        for i in range(1, r):
            new.append(prev[i - 1] + prev[i])

        new.append(1)
        triangle.append(new)

    return triangle
