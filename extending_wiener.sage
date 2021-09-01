from Crypto.Util.number import *
from tqdm import tqdm

def solver_2e(e1, e2, c1, c2, N):
    """
    solve for RSA in the Presence of 2 Small Decryption Exponents
    where alpha < 5 / 14.
    """

    alpha1 = 500
    for i in range(731, 682, -1):
        alpha = i / 2048
        M1 = int(N**0.5)
        M2 = int(N**(1+alpha))
        B = Matrix(ZZ, [ [N, -M1*N,      0,  N**2],
                         [0, M1*e1, -M2*e1, -e1*N],
                         [0,     0,  M2*e2, -e2*N],
                         [0,     0,      0, e1*e2] ])
        v = matrix(ZZ, B.LLL()[0])
        b = v * B^(-1)[0]
        phi = (b[1] / b[0] * e1).floor()
        try:
            m1 = pow(c1, inverse_mod(e1, phi), N)
            m2 = pow(c2, inverse_mod(e2, phi), N)
            if 'flag{' in str(long_to_bytes(m1)):
                print(long_to_bytes(m1) + long_to_bytes(m2))
                break
        except:
            pass

def solver_3e(e1, e2, e3, c1, c2, c3, n):
    """
    solve for RSA in the Presence of 2 Small Decryption Exponents
    where alpha < 2 / 5.
    """

    