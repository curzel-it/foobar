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