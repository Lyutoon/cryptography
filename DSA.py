from libnum import *

def signature(alpha, p, q, k, SHA3):
    gamma = pow(alpha, k, p) % q
    delta = (SHA3 + a * gamma) * invmod(k, q) % q
    print('[+] Get the signature:(', gamma,',', delta,')')
    return gamma, delta

def verify(gamma , delta, SHA3, q, p, beta, alpha):
    e1 = SHA3 * invmod(delta, q) % q
    e2 = gamma * invmod(delta, q) % q
    if pow(alpha, e1, p) * pow(beta, e2, p) % p % q == gamma:
        print('[+] Pass the verification!')
        return True
    print('[+] Invalid signature!')
    return False

if __name__ == '__main__':
    q = 101
    p = 7879
    a = 75
    alpha = 170
    beta = 4567
    k = 49
    SHA3 = 52
    gamma, delta = signature(alpha, p, q, k, SHA3)
    verify(gamma , delta, SHA3, q, p, beta, alpha)