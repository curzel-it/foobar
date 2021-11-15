def solution(x, y):
    matrix_size = x + y - 1
    greatest_in_matrix = sum(range(1, matrix_size+1))
    id = greatest_in_matrix - y + 1
    return str(id)
