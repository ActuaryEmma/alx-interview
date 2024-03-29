#!/usr/bin/python3
"""
that returns a list of lists of integers representing the Pascal’s triangle
"""


def pascal_triangle(n):
    """
    that returns a list of lists of integers representing the Pascal triangle
    """
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        triangle.append(row)
    for i in range(n):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    return triangle
