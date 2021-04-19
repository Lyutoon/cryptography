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

def crt(remainders, modules):
    if len(modules) == 1:
        return int(remainders[0])
    x = 0
    N = 1
    for module in modules:
        N *= module
    for i, module in enumerate(modules):
        if module == 1:
            continue
        Ni = N // module
        b = inverse(Ni, module)
        x += remainders[i] * Ni * b
    return int(x % N)

def shanks(n, g, h):
    m = int(pow(n-1, 0.5)) + 1
    l1 = []
    l2 = []
    for i in range(m+1):
        l1.append((i, pow(g, i*m, n)))
        l2.append((i, pow(g, -1*i, n) * h % n))
    l1.sort(key = lambda pair:pair[1])
    l2.sort(key = lambda pair:pair[1])
    i, j = 0, 0
    while(i < len(l1) and j < len(l2)):
        if l1[i][1] == l2[j][1]:
            x = l1[i][0] * m + l2[j][0]
            return x
        elif l1[i][1] > l2[j][1]:
            j += 1
        else:
            i += 1

def pohlig_hellman(n, g, h):
    print('[-] Start to factor the order...')
    factor = []
    order = n - 1
    for i in range(2, n):
        temp_factor = 1
        while order % i == 0:
            temp_factor *= i
            order //= i
        if temp_factor != 1:
            factor.append(temp_factor)
        if order == 1:
            break
    print('[+] Find the factors:', factor)
    print('[-] Start using shanks to solve DLP...')
    solutions = []
    for f in factor:
        temp_h = pow(h, n//f, n)
        temp_g = pow(g, n//f, n)
        solutions.append(shanks(n, temp_g, temp_h))
    print('[+] Find all the temp solutions', solutions)
    print('[-] Start to use CRT to solve DLP...')
    res = crt(solutions, factor)
    print('[+] Find the result:', res)
    return res


n = 28703
g = 5
h = 8563
pohlig_hellman(n,g,h)
print('--------'*10)
n = 31153
g = 10
h = 12611
pohlig_hellman(n,g,h)