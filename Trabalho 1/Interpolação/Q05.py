from weakref import ProxyTypes
import numpy as np


def poly(x,y):
    n = len(x)-1
    A =[]
    B =[]
    for xi in x:
        row = [1]
        for j in range(1, n+1):
            row.append(xi ** j)
        A.append(row)
    return np.linalg.solve(A, y)

def func_poly(x, coeffs):
    first=coeffs[0]
    return first + sum([ai * x ** j for j, ai in enumerate(coeffs[1:], 1)])

if __name__ == '__main__':
    #exemplo 1

    x = [0.398, 0.505, 1.26, 1.592, 1.887, 2.475, 2.94, 3.368, 3.95]
    y = [0.736, 0.842, 1.692, 1.951, 1.978, 1.079, 0.075, 0.426, 1.999]

    coeffs = poly(x,y)
    #print(coeffs)

    for x in (coeffs):
        print("%.16f," %x)
    def p(x):
        return func_poly(x,coeffs)

print("%.16f" %p(0.283)) #[0.283, 1.448, 2.31, 3.583]
print("%.16f" %p( 1.448))
print("%.16f" %p( 2.31))
print("%.16f" %p( 3.583))
