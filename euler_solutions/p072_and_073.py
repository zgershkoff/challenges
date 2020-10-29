# project euler problems 72 and 73

import sage.all
from sage.arith.misc import euler_phi

def p072():
    # We want to find all rational numbers between 0 and 1 with a
    # denominator of at most 1,000,000.
    # As the d denominator increases, the new rational numbers counted
    # will be equal in number to the integers coprime to d.
    # So, euler phi function.
    return sum(euler_phi(d) for d in range(2, 1_000_001))

def p073():
    # We want the rational numbers with denominators of at most 12000
    # between 1/3 and 1/2.
    # One approaches is to count the ones up to 1/2, then count the
    # ones up to 1/3, then subtract.
    # Due to symmetry, the rationals less than 1/2 will be half of those
    # counted by euler_phi - 1.
    # For the ones less than 1/3, I can brute force it.
    # There's theory behind this called Farey sequences, but brute
    # forcing is quicker than reading it.
    less_than_half = (sum(euler_phi(d) for d in range(2, 12001)) - 1)/2
    rationals = set()
    for d in range(2, 12001):
        for n in range(1, d):
            if n/d > 1/3:
                break
            rationals.add(n/d) # sage will treat this like a fraction
    less_than_third = len(rationals)
    return less_than_half - less_than_third


if __name__ == "__main__":
    print(p072())
    print(p073())
