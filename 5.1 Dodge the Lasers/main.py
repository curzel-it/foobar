"""
Well, I tried a bit of everything, and I eventually landed on integrals.
My idea was to calculate `integral( x * sqrt(2) )` by using some kind of geometrical approximation (Riemann sum), but that didn't work out, obviously.
Looking for alternative ways on how to approximate the integral on Wolfram, I landed on one of the search suggestions, `Beatty Sequences`.
https://en.wikipedia.org/wiki/Beatty_sequence
From the same wikipedia page I then got to the `Rayleigh Theorem`, and that was it
https://en.wikipedia.org/wiki/Beatty_sequence#Rayleigh_theorem

My original implementation for this used `Decimal`, but I was getting some approximation errors.
Finally I decided get this over with by just going with integers and no floating point!
"""

POW_10_100 = 10 ** 100

FACTOR = 4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727

def rayleigh(n):
    if n == 1: return 1        
    if n < 1: return 0
    m = (FACTOR * n) // POW_10_100
    return n*m + n*(n+1)/2 - m*(m+1)/2 - rayleigh(m)

def solution(n):
    r = rayleigh(int(n))
    return str(int(r))