import random
import numpy as np
import math


# k -> ordem
def dif_fin(x, x0, k):
    n = len(x)
    A = [[1]*n]
    B = [0]
    for i in range(1,n):
        row = [xi**i for xi in x]
        A.append(row)
        if i < k:
            B.append(0)
        else:
            bi = math.factorial(i) / math.factorial(i-k) * x0**(i-k)
            B.append(bi)
    return np.linalg.solve(A, B)

def aprox(coeffs,f,x):
    return sum(ci*f(xi) for ci, xi in zip(coeffs,x))


if __name__ == '__main__':


    x0 = -0.2023
    x = [-0.3969, -0.2747, -0.2449, -0.1161, -0.0257]

    def f(x):
        func = math.sin(math.cos(math.exp(-x)))
        return func

    n = len(x)
    k = 1 #ordem da derivada

    coeffs = dif_fin(x,x0,k)
    print(aprox(coeffs, f, x))

    
    