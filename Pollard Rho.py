import libnum

def gcd(a, b):
    if a == 0: return b
    if b == 0: return a
    while b:
        a, b = b, a % b
    return abs(a)

def Pollard_Rho(n):
    f = lambda x: (x*x + 1) % n
    x = 2
    _x = f(x)
    p = gcd(x - _x, n)
    count = 0
    while p == 1:
        x = f(x)
        _x = f(f(_x))
        p = gcd(x - _x, n)
        count += 1
    if p == n:
        print('[+] Failed')
    else:
        print('[+] Done! Find p:', p)
        print('[+] n =', p, '*', n//p)
        print('[+] Totle iteration time:',count)
        return p
Pollard_Rho(262063)
print('*' * 30)
Pollard_Rho(9420457)
print('*' * 30)
Pollard_Rho(181937053)