"""
In order to solve in O(n) we need to traverse the list only once.
We do so by keeping track of a window of values (two indeces) which we will move accordingly.
"""

def solution(l, t):
    start = 0
    end = start + 1

    while end <= len(l):
        window_sum = sum(l[start:end])
        if window_sum == t:
            return [start, end-1]

        if window_sum > t:
            start += 1
            end = start + 1
        else:
            end += 1
    return [-1, -1]
