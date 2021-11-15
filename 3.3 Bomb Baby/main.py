"""
Starting from the desidered number of bombs, M and F, we do a series of divisions.
Divisions, in this case, should be considered a series of subtractions, as we keep the rest of the division as the term for the next cycle.
If we reach 1, 1, it is possible to reach the given number of bombs, and we have just found the best solution, else it is impossible.
"""

def nsolution(m, f):
    g = 0

    while f >= 1:
        if f == 1:
            return g + m - 1
        g += m // f
        m, f = f, m % f
    return None


def solution(s1, s2):
    m, f = int(s1), int(s2)
    m, f = (m, f) if m > f else (f, m)
    if m == f == 1:
        return '0'
    if m <= 0 or f <= 0:
        return 'impossible'
    n = nsolution(m, f)
    return str(n) if n else 'impossible'

    # Note to self:
    # Following does not work with Python 2.7!!
    # return '{:.0f}'.format(n) if n else 'impossible'


if __name__ == '__main__':
    import time
    import sys

    values = [
        (-1, 1, 'impossible'),
        (2, 1, '1'),
        (3, 4, '3'),
        (2, 4, 'impossible'),
        (4, 7, '4'),
        (139, 1222, '21'),
        (25995, 15904, '23'),
        (25995322, 159042343994, 'impossible'),
        (
            122051587417034903144854863871090686829550780619301,
            196563109715132368390217809010624430379768076476480,
            '283'
        ),
        (
            255700741502252720628394795916288081409991931766566827134810177186598086745859757299878250805764668189604954139051010054982695299270966123628887244056171787480513131055631060,
            48268218189059955497575472256060715718589629541164214279256098473453400705169612371092703317756710968762271874275570356129696750945251794576821533646867762666917562683076851,
            '1001'
        )
    ]

    start = time.time()

    failed = []
    for i in range(4000):
        for m, f, s in values:
            n = solution(m, f)
            if i == 0 and n != s:
                failed.append((m, f, s, n))

    end = time.time()

    if len(failed):
        print("Failed:")
        for m, f, s, n in failed:
            print("M:", m, "F:", f, "Expected:", s, "got:", n)
    else:
        print("All passed!")

    print("Time:", end - start)
