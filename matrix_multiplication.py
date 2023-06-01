"""MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

"""
Module supplying a function for matrix multiplication.
Numpy is way better, I'm strictly trying to solidify my understanding
by implementing it in Python.
"""


def multiply_matrices(m_1: list, m_2: list) -> list:
    """
    Parameters
    ----------
    m_1 : list of lists =>
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

    m_2 : list of lists =>
    [[10, 11, 12],
     [13, 14, 15],
     [17, 18, 19]]

    Returns
    ------
    transformation : list of lists =>
    [[ 87,  93,  99],
     [207, 222, 237],
     [327, 351, 375]]
    """
    if len(m_1[0]) != len(m_2):
        raise ValueError("Size mismatch: m_1 columns do not match m_2 rows")
    transformation = [[] for _ in m_1]
    for column_idx, _ in enumerate(m_2[0]):
        for i, m1_row in enumerate(m_1):
            m_2_column = [m2_row[column_idx] for m2_row in m_2]
            positional_sum = sum(a * b for a, b in zip(m1_row, m_2_column))
            transformation[i].append(positional_sum)
    return transformation
