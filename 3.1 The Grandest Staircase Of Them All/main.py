"""
We recursively place bricks to form a new step of the stair case.
When the number of bricks left is zero we store the combination.
After each step, the max and min height of the next step can be calculated in order to reduce the number of possibilities.
"""

import math

stored_solutions_count = {}


def solution(n, previous=None):

    solutions = 0
    max_height = min((previous - 1) if previous else n, n)
    # There is for sure another value but I have no idea
    min_height = int(math.floor(math.sqrt(n))) - 1

    for i in range(max_height, min_height, -1):
        bricks_left = n - i

        if bricks_left == 0 and previous is not None:
            solutions += 1
        elif bricks_left > 0:
            key = (bricks_left, i)
            if stored_solutions_count.get(key):
                solutions += stored_solutions_count[key]
            else:
                solutions += solution(bricks_left, i)

    stored_solutions_count[(n, previous)] = solutions
    return solutions