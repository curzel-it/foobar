POW_10_100 = 10 ** 100

# This should ideally be `sqrt(2) - 1`
# No idea if it was an issue with representation or what, but I just opted for putting an integer constant to get it over with!
# So... (sqrt(2) - 1) * 10**100
FACTOR = 4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727

def rayleigh(n):
    if n == 1: return 1        
    if n < 1: return 0
    m = (FACTOR * n) // POW_10_100
    return n*m + n*(n+1)/2 - m*(m+1)/2 - rayleigh(m)

def solution(n):
    r = rayleigh(int(n))
    return str(int(r))