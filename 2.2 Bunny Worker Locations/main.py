"""
The smallest square (or matrix) large enough to contain the given coordinates has size `x + y +1`.
The biggest number in a matrix of size N, with given rules is `n + n-1 + n-2 + ... + 1`.
Given the biggest number, we can just subtract y to "move" to the correct id.
"""

def solution(x, y):
    matrix_size = x + y - 1
    greatest_in_matrix = sum(range(1, matrix_size+1))
    id = greatest_in_matrix - y + 1
    return str(id)
