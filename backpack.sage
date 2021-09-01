# solve for low density Merkle–Hellman cryptosystem

import math

def solve(pk, ct):
    n = len(pk)
    N = ceil(sqrt(n)/2)

    d = n / math.log(max(pk), 2)
    assert CDF(d) < 0.9408

    M = Matrix.identity(n) * 2

    last_row = [1 for x in pk]
    M_last_row = Matrix(ZZ, 1, len(last_row), last_row)

    last_col = pk
    last_col.append(ct)
    M_last_col = Matrix(ZZ, len(last_col), 1, last_col)*2*N

    M = M.stack(M_last_row)
    M = M.augment(M_last_col)

    #  (n+1) * (n+1)
    #  2 0 ... 0 pk_0*2N
    #  0 2 ... 0 pk_1*2N
    #  . . ... .  ...
    #  0 0 ... 2 pk_n*2N
    #  1 1 ... 1  ct*2N

    X = M.LLL()
    # print(X)

    sol = []
    for i in range(n + 1):
        testrow = X.row(i).list()[:-1]
        if set(testrow).issubset([-1, 1]):
            for v in testrow:
                if v == 1:
                    sol.append(0)
                elif v == -1:
                    sol.append(1)
            break

    assert len(sol) == n
    assert ct == sum([x * y for (x, y) in zip(sol, pk)])
    print(long_to_bytes(int("".join(list(map(str, sol[::-1]))), 2)))
