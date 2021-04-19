def jacobi1(a, n):
    assert n >= 1 and n & 1
    res = 1
    a %= n
    while a != 0:
        while a & 1 == 0:
            # If n % 8 = 3 or 5 then we knwo that (n^2-1)/8 is odd.
            if n % 8 == 3 or n % 8 == 5:
                res = -res
            a >>= 1
        a, n = n, a
        # If a % 4 = 3 and n % 4 = 3 then we know that (a-1)(n-1)/4 is odd.
        if a % 4 == 3 and n % 4 == 3:
            res = -res
        a %= n
    if n == 1:
        return res
    return 0

print(jacobi1(610, 987))
print(jacobi1(20964, 1987))
print(jacobi1(1234567,11111111))
