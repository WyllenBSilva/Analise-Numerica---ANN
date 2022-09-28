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

    x = [-3.63, -2.64, -1.536, -0.838, 0.196, 1.109, 1.727, 2.858, 3.454]
    y = [4.016, 3.829, 0.71, 2.578, 3.932, 3.256, 2.195, 4.738, 3.093]
    coeffs = poly(x,y)
    #print(coeffs)

    for x in (coeffs):
        print("%.16f," %x)
    def p(x):
        return func_poly(x,coeffs)


print("%.16f" %p(-1.671)) #values = [-1.671, -1.359, -0.191, 0.506]
print("%.16f" %p( -1.359))
print("%.16f" %p(  -0.191))
print("%.16f" %p( 0.506))
