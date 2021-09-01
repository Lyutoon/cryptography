from sage.rings.finite_rings.integer_mod import square_root_mod_prime

def SquareRoots(a, p):
    """
    Solve equation that x^2 = a mod p where p is a prime number
    Return all roots 
    """
    x1 = square_root_mod_prime(mod(a, p))
    x2 = p - x1
    return [x1, x2]