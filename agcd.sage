# AGCD: `xi = p*qi+ri` for 1<=i<=t, where ri is small.
#        Given some xi, solve for common divisor p.

from Crypto.Util.number import *


def SDA_solver(xs, rho):
    """
    Basic idea: xi / x0 = qi / q0
    Construct lattice to attack.
    B = [2^(rho+1)  x1   x2  ....  xt]
        [           -x0              ]
        [                -x0         ]
        [                   .        ]
        [                     .      ]
        [                       .    ]
        [                         -x0]
    v = (q0, q1, ..., qt)B
      = (q0*2^(rho+1), q0r1-q1r0, ..., q0rt-qtr0)
    B.LLL() to solve for q0 so we can solve for p
    """

    # 1. Construct lattice
    t = len(xs) - 1
    B = Matrix(ZZ, t+1, t+1)
    for i in range(t+1):
        B[i, i] = -xs[0]
        if i == 0:
            B[0, i] = 2^(rho+1)
        else:
            B[0, i] = xs[i]
    # 2. LLL and find p
    v = B.LLL()[0]
    q0 = v[0] // 2^(rho+1)
    p = xs[0] // q0
    return p

def MP_solver(xs, rho):
    """
    Multiivariate polynomial approach (MP)
    similar to Multiivariate-coppersmith construction
    Using polynomials to construct lattice and solve for p
    """

    X = 1<<rho
    m = len(xs)
    PR = PolynomialRing(ZZ, names=[str('x%d' % i) for i in range(1, m+1)])
    h = 3
    u = 1
    variables = PR.gens()
    gg = []
    monomials = [variables[0] ** 0]
    for i in range(m):
        gg.append(xs[i] - variables[i])
        monomials.append(variables[i])
    print(len(monomials), len(gg))
    print('monomials:', monomials)

    B = Matrix(ZZ, len(gg), len(monomials))
    for ii in range(len(gg)):
        for jj in range(len(monomials)):
            if monomials[jj] in gg[ii].monomials():
                B[ii, jj] = gg[ii].monomial_coefficient(monomials[jj]) * monomials[jj]([X] * m)
    B = B.LLL()

    new_poly = []
    for i in range(len(gg)):
        tmp_poly = 0
        for j in range(len(monomials)):
            tmp_poly += monomials[j](variables) * B[i, j] / monomials[j]([X] * m)
        new_poly.append(tmp_poly)
    
    if len(new_poly) > 0:
        Ideal = ideal(new_poly[:m-1])
        GB = Ideal.groebner_basis()
        function_variables = var([str('y%d' % i) for i in range(1, 1 + m)])
        res = solve([pol(function_variables) for pol in GB], function_variables)
        print('got %d basis' % len(GB))
        print('solved result:')
        print(res)
        for tmp_res in res:
            PRRR.<x, y> = PolynomialRing(QQ)
            q = abs(PRRR(res[0][0](x, y)).coefficients()[0].denominator())
            p = xs[-1] // q
            # print(p)
            return p

def generate_testcase(rbits, pbits):
    rbit = int(rbits)
    pbit = int(pbits)
    p = getPrime(pbit)
    ns = [p*getPrime(pbit) + getPrime(rbit) for i in range(5)]
    return p, ns

if __name__ == '__main__':
    p, ns = generate_testcase(300, 512)
    recover_p_SDA = SDA_solver(ns, 300)
    recover_p_MP = MP_solver(xs = ns, rho = 300)
    if p == recover_p_SDA:
        print('Pass SDA method!!')
    if p == recover_p_SDA:
        print('Pass SDA method!!')