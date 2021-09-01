from Crypto.Util.number import *
from functools import reduce

# LCG: s_{i+1} = a*s_{i} + b mod N

def lcg_attack_without_b(s, a, N):
    if len(s) < 2:
        print('invalid input length!')
        exit(0)
    b = (s[1] - a*s[0]) % N
    return (a, b, N)

def lcg_attack_without_ab(s, N):
    if len(s) < 3:
        print('invalid input length!')
        exit(0)
    a = (s[2] - s[1]) * inverse(s[1] - s[0], N) % N
    return lcg_attack_without_b(s, a, N)

def lcg_attack_withoutAll(s):
    if len(s) < 6:
        print('invalid input length!')
        exit(0)
    xx = [s[i] - s[i-1] for i in range(1, len(s))]
    yy = [xx[i+1] * xx[i-1] - xx[i] * xx[i] for i in range(1, len(xx)-1)]
    N = abs(reduce(GCD, yy))
    return lcg_attack_without_ab(s, N)

if __name__ == '__main__':
    a = getPrime(177)
    b = getPrime(333)
    N = getPrime(512)
    seed = getPrime(111)
    s = [seed]
    for i in range(10):
        s.append((a*s[i] + b) % N)
    res = lcg_attack_withoutAll(s)
    if res == (a, b, N):
        print("Pass!")