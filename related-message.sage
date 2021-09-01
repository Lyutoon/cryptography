import sys
from Crypto.Util.number import *
import numpy as np

"""
Condition 1: 
Given enc(m) and enc(m+delta) construct f1 = x^e - c1, f2 = (x+delta)^e - c2
Find gcd(f1, f2) which is a monimal in format: am + b = 0 from which we can find m
"""

pgcd = lambda g1, g2: g1.monic() if not g2 else pgcd(g2, g1%g2)

# HGCD Algorithm From rkm0959 which is faster than the common gcd algorithm.
def HGCD(a, b):
    if 2 * b.degree() <= a.degree() or a.degree() == 1:
        return 1, 0, 0, 1
    m = a.degree() // 2
    a_top, a_bot = a.quo_rem(x^m)
    b_top, b_bot = b.quo_rem(x^m)
    R00, R01, R10, R11 = HGCD(a_top, b_top)
    c = R00 * a + R01 * b
    d = R10 * a + R11 * b
    q, e = c.quo_rem(d)
    d_top, d_bot = d.quo_rem(x^(m // 2))
    e_top, e_bot = e.quo_rem(x^(m // 2))
    S00, S01, S10, S11 = HGCD(d_top, e_top)
    RET00 = S01 * R00 + (S00 - q * S01) * R10
    RET01 = S01 * R01 + (S00 - q * S01) * R11
    RET10 = S11 * R00 + (S10 - q * S11) * R10
    RET11 = S11 * R01 + (S10 - q * S11) * R11
    return RET00, RET01, RET10, RET11
    
def PGCD(a, b):
    print(a.degree(), b.degree())
    q, r = a.quo_rem(b)
    if r == 0:
        return b
    R00, R01, R10, R11 = HGCD(a, b)
    c = R00 * a + R01 * b
    d = R10 * a + R11 * b
    if d == 0:
        return c.monic()
    q, r = c.quo_rem(d)
    if r == 0:
        return d
    return PGCD(d, r)

"""
Condition 2:
Given many message which is related such as:
Given m = a*b + c<<20 and give that enc(a), enc(b), enc(c), enc(m)
Try to find m. 
Exactly, we can use groebner basis to solve these related equation
since groebner basis can automatically separate the parameters 
and also we can use this method to solve condition 1.
"""

def get_GB(polys):
    I = ideal(polys)
    return I.groebner_basis()[0]
