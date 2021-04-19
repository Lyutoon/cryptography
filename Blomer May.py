import gmpy2
from libnum import *

def gen_q(a, b):
    r0, r1 = a, b
    q_lst = []
    while r0 % r1 != 0:
        q_lst.append(r0 // r1)
        r0, r1 = r1, r0 % r1
    q_lst.append(r0 // r1)
    return q_lst

def get_convergents(q):
    convergents = [(q[0], 1)]
    for i in range(2, len(q) + 1):
        q_partion = q[0:i]
        denom = q_partion[-1]
        num = 1
        for _ in range(-2, -len(q_partion), -1):
            num, denom = denom, q_partion[_] * denom + num
        num += denom * q_partion[0]
        convergents.append((num, denom))
    return convergents

def BlomerMay(e, n):
    """
    Blomer May attack
    Input: public key (e, N)
    Output: p, q
    Situation: N = pq, q < p < 2q, ex-y*phi(N) = z with gcd(x, y) = 1 and
               xy < 3(p+q)N / 2((p-q)^(1/4)+3(p+q)^2) and 
               |z| < (p-q)N^(1/4)y / 3(p+q)
    """
    q_lst = gen_q(e, n)
    convergents = get_convergents(q_lst)
    for y, x in convergents:
        if y != 0:
            T = n + 1 - (e*x) // y
            pho = (T + int(gmpy2.iroot(T**2 - 4*n, 2)[0])) // 2
            for i in range(-2**5, 2**5):
                p = pho + i
                if n > p > 1 and n % p == 0:
                    q = n // p			 
                    print('[+] p =', p)
                    print('[+] q =', q)
                    return p, q

def main():
    e = 372077403420031165815439199213704344304928202869941592969972103002464355333911024937074871410825817568355544126574173758702600945390438495248751733573391345292294888885607465578329781858741122278411513362633310583564023669185613282939355138576537165757775740881908805743008022348524049466231348651228609449357106436669219
    n = 470335762637936005588762180827192207993663594416060284974932410896705386687847439702920143090437462997342000428130417147164245577372958674672171462397851600930104979198327224831772288314005311036009419876584852939180439595289349509330868790367408195151323961061772542485151690708678904080061050887466315542337191307236199
    p, q = BlomerMay(e, n)
    assert p * q == n

main()