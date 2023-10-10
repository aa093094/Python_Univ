# This program is about finding approximated x that fulfills f(x) = 0

import math

def Bisect(xl, xu, es, imax):
    iter = 0
    xr = xl
    ea = 0.0

    while True:
        xrold = xr
        xr = (xl + xu) / 2
        fr = f(xr)
        iter += 1

        if xr != 0:
            ea = abs((xr - xrold) / xr) * 100

        test = f(xl) * fr

        if test < 0:
            xu = xr
        elif test > 0:
            xl = xr
        else:
            ea = 0

        if ea < es or iter >= imax:
            return xr
        print(iter, " : ", xr)

# t, v, m are parameters. Below is a example.
def f(c):
    g = 9.81
    t = 10
    v = 40
    m = 68.1
    return g * m * (1 - math.exp(-c / m * t)) / c - v

# Changing es and imax to get the different result
xl = 1.0
xu = 100.0
es = 0.000001
imax = 1000

result = Bisect(xl, xu, es, imax)
print("Approximate root:", result)
