from math import sqrt
from libnum import gcd
from random import *
from itertools import product
from Crypto.Util.number import *

def gen_w(n):
    l = int(pow(n, 1/2))
    temp = product([i+1 for i in range(l)], repeat=2)
    w = {}
    for i in range(n):
        w[i+1] = tuple(next(temp))
    return w

def Quary(i, n):
    w = gen_w(n)
    l = int(sqrt(n))
    assert l**2 == n
    p = getPrime(512)
    q = getPrime(512)
    N = p * q
    g = N + 1
    rk = (p-1) * (q-1)
    u, v = w[i]
    r = []
    for _ in range(l):
        temp_r = randint(1, N-1)
        while gcd(temp_r, N) != 1:
            temp_r = randint(1, N-1)
        r.append(temp_r)
    q = []
    for i in range(l):
        if i+1 == v:
            temp_y = g * pow(r[i], N, N**2) % (N**2)
        else:
            temp_y = pow(r[i], N, N**2)
        q.append(temp_y)
    return q, rk, N


def Answer(q, N, x, n):
    w = gen_w(n)
    l = int(sqrt(n))
    X = [[0]*l for _ in range(l)]
    for j in range(1, n+1):
        u, v = w[j]
        X[u-1][v-1] = int(x[j-1])
    a = []
    for s in range(l):
        a_s = 1
        for i in range(l):
            a_s = a_s * pow(q[i], X[s][i], N**2) % N**2
        a.append(a_s)
    return a


def Reconstruct(i, rk, a, N, n):
    w = gen_w(n)
    u, v = w[i]
    a_u = a[u-1]
    z = (pow(a_u, rk, N**2) - 1) % N**2
    x = (z//N) * (inverse(rk, N)) % N
    return x

if __name__ == '__main__':
    """
    Since that n is a known variable for every certain x and it is known to all users and servers.
    So in order to make my process can due with different n, I add a parameter called n to satisfy different n.
    In reality n is a fixed number before we run program, so I pass a n in order to due with different n.
    In this way I can due with all n that satisfies l^2 = n.
    """
    # n = 9
    # x = '010101010'
    n = 16
    x = '1001100111001101'
    r = ''
    for i in range(n):
        q, rk, N = Quary(i+1, n)
        a = Answer(q, N, x, n)
        xi = Reconstruct(i+1, rk, a, N, n)
        r += str(xi)
    print('[+] After taversing all the index, the user will get:', r)
    print('[-] After taversing all the index, the user should get:', x)
    if r == x:
        print('[+] Congratulations! Users can get the correct data!')