from sympy import *

x, y = symbols("x y")


def take_integral(func, b1, b2, prec):
    integral = 0
    delta = (b2 - b1)
    print(delta)
    k = b1 + (delta / prec)
    for i in range((delta * prec) + prec):
        integral += func.subs(x, k) * k
        print(integral)
        k += delta / prec
    return integral


print(take_integral(3**x - 9, 0, 1, 100))




