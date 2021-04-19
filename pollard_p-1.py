#import libnum
from random import randint
def gcd(a, b):
    if a == 0: return b
    if b == 0: return a
    while b:
        a, b = b, a % b
    return abs(a)

# method 1 : traverse to find min_B and try to factor n
def pollard_p_1(n):
    B = 2
    while True: 
        a = 2
        for i in range(2, B+1):
            a = pow(a, i, n)
        d = gcd(a-1, n)
        if d != 1:
            print('[+] Method1 Find p:', d)
            print('[+] Method1 Find min_B:', B)
            return d, B
        B += 1
# method 2 : random choose B and factor n
# but if we want to find the min_B we need to traverse or binary search.
# we can also put these two method together.
def pollard_p_2(n):
    B = randint(2, n)
    while True: 
        a = 2
        for i in range(2, B+1):
            a = pow(a, i, n)
        d = gcd(a-1, n)
        if d == 1:
            B = randint(B+1, n)
        elif d == n:
            B = randint(2, B-1)
        else:
            print('[+] Method2 Find p:', d)
            return d 
n1 = 262063
n2 = 9420457
p1 = pollard_p_1(n1)[0]
p2 = pollard_p_1(n2)[0]
pollard_p_2(n1)
pollard_p_2(n2)
print('[+] n1 = ',p1,'*',n1//p1)
print('[+] n1 = ',p2,'*',n2//p2)