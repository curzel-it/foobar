"""
We find primes and add them to a string one by one, until the string is long enough to generate the required id.
"""

def solution(i):
    return primes_string(i+5)[i:i+5]

def primes():
    D = {}
    q = 2

    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

def primes_string(min_length):
    s = ''
    for prime in primes():
        s += str(prime)
        if len(s) >= min_length:
            return s
