def gcd(a, b):
    if a == 0: return b
    if b == 0: return a
    while b:
        a, b = b, a % b
    return abs(a)

def xgcd(a, b):
    if a == 0: return 0, 1, b
    if b == 0: return 1, 0, a
    px, ppx = 0, 1
    py, ppy = 1, 0
    while b:
        q = a // b
        a, b = b, a % b
        x = ppx - q * px
        y = ppy - q * py
        ppx, px = px, x
        ppy, py = py, y
    return ppx, ppy, a

def inverse(a, n):
    x, y, g = xgcd(a, n)
    if g == 1:
        return x % n

def Pollard_Rho(p, g, h, n):
    f = lambda x, a, b: (h*x%p, a, (b+1)%n) if x % 3 == 1 else((x**2%p, 2*a%n, 2*b%n) if x % 3 == 0 else (g*x%p, (a+1)%n, b))
    x0 = f(1, 0, 0)
    x1 = f(*x0)
    count = 1
    while(x0[0] != x1[0]):
        x0 = f(*x0)
        x1 = f(*f(*x1))
        count += 1
    if gcd(x1[2] - x0[2], n) == 1:
        res = (x0[1] - x1[1]) * inverse(x1[2]-x0[2], n) % n
        print('[+] Find DLP solution:', res)
        print('[+] The smallest i is:', count)
        return res

p = 458009
n = 57251
g = 2
h = 56851
Pollard_Rho(p,g,h,n)