import random
from itertools import product

def gen_w(n):
    l = int(pow(n, 1/4))
    temp = product([i+1 for i in range(l)], repeat=4)
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

def Quary(i, n):
    """
    Generate all quary that will be needed to send to servers in one function.
    """
    w = gen_w(n)
    l = int(pow(n, 1/4))
    assert l ** 4 == n
    i1, i2, i3, i4 = [{_} for _ in w[i]]
    _i1, _i2, _i3, _i4 = w[i]
    temp_l = [i+1 for i in range(l)]
    subset = SubSets(temp_l)
    s10 = random.choice(subset)
    s20 = random.choice(subset)
    s30 = random.choice(subset)
    s40 = random.choice(subset)
    s11 = sym_dif(s10, i1)
    s21 = sym_dif(s20, i2)
    s31 = sym_dif(s30, i3)
    s41 = sym_dif(s40, i4)
    q0000 = (s10, s20, s30, s40)
    q1111 = (s11, s21, s31, s41)
    q1000 = (s11, s20, s30, s40)
    q0111 = (s10, s21, s31, s41)
    return (q0000, q1111, q1000, q0111)

def Answer(q: tuple, x:str, n):
    w = gen_w(n)
    l = int(pow(n, 1/4))
    y = {}
    for i in range(n):
        y[w[i+1]] = int(x[i])
    s1, s2, s3, s4 = q
    def cal_a():
        S = list(product(s1, s2, s3, s4))
        res = 0
        for para in S:
            res += y[tuple(para)]
        return res % 2
    a = cal_a()
    def cal_As(q):
        A1 = []
        A2 = []
        A3 = []
        L = [{i+1} for i in range(l)]
        for s in (L):
            S1 = list(product(q[0], sym_dif(q[1], s), q[2], q[3]))
            S2 = list(product(q[0], q[1], sym_dif(q[2], s), q[3]))
            S3 = list(product(q[0], q[1], q[2], sym_dif(q[3], s))) 
            res1, res2, res3 = 0, 0, 0
            for para1 in S1:
                res1 += y[tuple(para1)]
            A1.append(res1 % 2)
            for para2 in S2:
                res2 += y[tuple(para2)]
            A2.append(res2 % 2)
            for para3 in S3:
                res3 += y[tuple(para3)]
            A3.append(res3 % 2)
        return (A1, A2, A3)
    A1, A2, A3 = cal_As(q)
    return (a, A1, A2, A3)

def Reconstruct(data: tuple, i: int, n):
    w = gen_w(n)
    _i1, _i2, _i3, _i4 = w[i]
    a0000, A0100, A0010, A0001, a1111, A1011, A1101, A1110, a1000, A1100, A1010, A1001, a0111, A0011, A0101 , A0110 = data
    xi = (a0000 + a1111 + a0111 + a1000  + A0100[_i2-1] + A0010[_i3-1] + A0001[_i4-1] + A1011[_i2-1] + A1101[_i3-1] 
    + A1110[_i4-1] + A0011[_i2-1] + A0101[_i3-1] + A0110[_i4-1] + A1100[_i2-1] + A1010[_i3-1] + A1001[_i4-1]) % 2
    return xi

if __name__ == '__main__':
    """
    Since that n is a known variable for every certain x and it is known to all users and servers.
    So in order to make my process can due with different n, I add a parameter called n to satisfy different n.
    In reality n is a fixed number before we run program, so I pass a n in order to due with different n.
    In this way I can due with all n that satisfies l^4 = n.
    """
    m = '0100110011010011'
    r = ''
    n = 16
    m = '010111011' * 9
    n = 81
    for i in range(1, n+1):
        q0000, q1111, q1000, q0111 = Quary(i, n)
        data0 = Answer(q0000, m, n)
        data1 = Answer(q1111, m, n)
        data2 = Answer(q1000, m, n)
        data3 = Answer(q0111, m, n)
        data = data0 + data1 + data2 + data3
        x = Reconstruct(data, i, n)
        r += str(x)
    print('[+] After taversing all the index, the user will get:', r)
    print('[-] After taversing all the index, the user should get:', m)
    if r == m:
        print('[+] Congratulations! Users can get the correct data!')

    