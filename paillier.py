from libnum import *

def encrypt(x, r, p, q):
    n = p * q
    g = n + 1
    c = pow(g, x, n**2) * pow(r, n, n**2) % n**2
    return c

def decrypt(y, p, q):
    n = p * q
    phi = (p-1) * (q-1)
    m = ((pow(y, phi, n**2) - 1) // n) * invmod(phi, n) % n
    return m

if __name__ == '__main__':
    p = 1041857
    q = 716809
    n = p * q
    x1 = 726095811532
    x2 = 450864083576
    r1 = 270134931749
    r2 = 378141346340
    y1 = encrypt(x1, r1, p, q)
    y2 = encrypt(x2, r2, p, q)
    print('[+] y1 =', y1)
    print('[+] y2 =', y2)
    y3 = (y1 * y2) % n**2
    x3 = decrypt(y3, p, q)
    print('[+] x3 =', x3)
    print('[+] (x1 + x2)mod n =', (x1 + x2) % n)