import random
from itertools import product

def gen_w(n):
    l = int(pow(n, 1/3))
    temp = product([i+1 for i in range(l)], repeat=3)
    w = {}
    for i in range(n):
        w[i+1] = tuple(next(temp))
    return w


def SubSets(Se):
    S = list(Se)
    N = len(S)
    res = []
    for i in range(2 ** N):
        combo = []
        for j in range(N):
            if(i>>j) % 2:
                combo.append(S[j])
        res.append(set(combo))
    return res

def sym_dif(s1: set, s2: set):
    return (s1-s2) | (s2-s1)

def cal_a(s1, s2, s3, y):
    S = list(product(s1, s2, s3))
    res = 0
    for para in S:
        res += y[tuple(para)]
    return res % 2

def cal_As(q, y, n):
    l = int(pow(n, 1/3))
    A1 = []
    A2 = []
    A3 = []
    L = [{i+1} for i in range(l)]
    for s in L:
        S1 = list(product(q[0].symmetric_difference(s), q[1], q[2]))
        S2 = list(product(q[0], q[1].symmetric_difference(s), q[2]))
        S3 = list(product(q[0], q[1], q[2].symmetric_difference(s)))
        res1 = 0
        res2 = 0
        res3 = 0
        for para in S1:
            res1 += y[para]
        A1.append(res1 % 2)
        for para in S2:
            res2 += y[para]
        A2.append(res2 % 2)
        for para in S3:
            res3 += y[para]
        A3.append(res3 % 2)
    return (A1, A2, A3)

def Quary(i, n):
    """
    Generate all quary that will be needed to send to servers in one function.
    """
    w = gen_w(n)
    l = int(pow(n, 1/3))
    assert l ** 3 == n
    i1, i2, i3 = [{_} for _ in w[i]]
    _i1, _i2, _i3 = w[i]
    temp_l = [i+1 for i in range(l)]
    subset = SubSets(temp_l)
    #subset = [set(), {1}, {2}, {1,2}]
    s10 = random.choice(subset)
    s20 = random.choice(subset)
    s30 = random.choice(subset)
    s11 = s10.symmetric_difference(i1)
    s21 = s20.symmetric_difference(i2)
    s31 = s30.symmetric_difference(i3)
    q000 = (s10, s20, s30)
    q111 = (s11, s21, s31)
    return (q000, q111)

def Answer(q: tuple, x:str, n):
    """
    Calculate the data from the given index i and servers' x.
    """
    w = gen_w(n)
    y = {}
    for i in range(n):
        y[w[i+1]] = int(x[i])
    s1, s2, s3 = q 
    a = cal_a(s1, s2, s3, y)
    A1, A2, A3 = cal_As(q, y, n)
    return (a, A1, A2, A3)

def Reconstruct(data: tuple, i: int, n: int):
    """
    Get the result from the reply from servers.
    """
    w = gen_w(n)
    _i1, _i2, _i3 = w[i]
    a000, A100, A010, A001, a111, A011, A101, A110 = data
    xi = (a000 + A100[_i1 - 1] + A010[_i2 - 1] + A001[_i3 - 1] + a111 + A011[_i1 - 1] + A101[_i2 - 1] + A110[_i3 - 1]) % 2
    return xi

if __name__ == '__main__':
    """
    Since that n is a known variable for every certain x and it is known to all users and servers.
    So in order to make my process can due with different n, I add a parameter called n to satisfy different n.
    In reality n is a fixed number before we run program, so I pass a n in order to due with different n.
    In this way I can due with all n that satisfies l^3 = n.
    """
    n = 27
    x = '011011010010011001110110110'
    r = ''
    for i in range(1, n+1):
        q000, q111 = Quary(i, n)
        data0 = Answer(q000, x, n)
        data1 = Answer(q111, x, n)
        data = data0 + data1
        xi = Reconstruct(data, i, n)
        r += str(xi)
    print('[+] After taversing all the index, the user will get:', r)
    print('[-] After taversing all the index, the user should get:', x)
    if r == x:
        print('[+] Congratulations! Users can get the correct data!')
