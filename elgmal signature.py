from libnum import *

def solve():
    p = 31847
    x1 = 8990
    s1 = (23972, 31396)
    x2 = 31415
    s2 = (23972, 20481)
    g = 5
    h = 25703
    try:
        k = (x1 - x2) * invmod(s1[1] - s2[1], p-1) % (p - 1)
        print('[+] Find k:', k)
    except:
        up = x1 - x2
        down = s1[1] - s2[1]
        d = gcd(down, p-1)
        _down = down // d
        _up = up // d
        _p = (p-1) // d
        _k = _up * invmod(_down, _p) % _p
        for i in range(d + 1):
            k = (_k + i * _p) % (p-1)
            if pow(g, k, p) == s1[0]:
                print('[+] Find k:', k)
                break
            if i == d:
                print('[x] No solution!!')
    try:
        a = invmod(s1[0], p-1) * (x1 - s1[1] * k) % (p-1)
        print('[+] Find a:', a)
    except:
        d = gcd(s1[0], p-1)
        temp = x1 - s1[1] * k
        _gamma = s1[0] // d
        _temp = temp // d
        _p = (p-1) // d
        _a = invmod(_gamma, _p) * _temp % _p
        for i in range(d + 1):
            a = (_a + i * _p) % (p-1)
            if pow(g, a, p) == h:
                print('[+] Find a:', a)
                break
            if i == d:
                print('[x] No solution!!')
    return k, a

if __name__ == '__main__':
    solve()