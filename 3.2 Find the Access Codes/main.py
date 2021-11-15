"""
We go through the list, and for each number we store all `previous divisors` and `successive multiples`.
For each number y, we add n solutions, where in are the combinations (x,y,z), where x is a previous divisor and z a successive multiple.
This means that, for each number, the number of combinations to add is the `number of divisors * number of multiples`.
"""

def solution(l):
    solutions = 0

    for i, n in enumerate(l[1:-1]):

        divisors = 0
        for d in l[:i+1]:
            if n % d == 0:
                divisors += 1

        multiples = 0
        for m in l[i+2:]:
            if m % n == 0:
                multiples += 1

        solutions += divisors * multiples

    return solutions