import math
from ..maths.find_order_simple import find_order
from ..maths.euler_totient import euler_totient


"""
For positive integer n and given integer a that satisfies gcd(a, n) = 1,
a is the primitive root of n, if a's order k for n satisfies k = ϕ(n).
Primitive roots of certain number may or may not be exist.
If so, return empty list.
"""


def find_primitive_root(n):
    if n == 1:
        """ Exception Handeling :
        0 is the only primitive root of 1 """
        return [0]
    else:
        phi = euler_totient(n)
        p_root_list = []
        """ It will return every primitive roots of n. """
        for i in range(1, n):
            if math.gcd(i, n) != 1:
                """ To have order, a and n must be
                relative prime with each other. """
            else:
                order = find_order(i, n)
                if order == phi:
                    p_root_list.append(i)
                else:
                    continue
        return p_root_list
