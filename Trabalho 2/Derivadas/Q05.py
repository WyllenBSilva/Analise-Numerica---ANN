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


    x0 = 2.1587
    x = [1.9642, 1.9951, 2.0773, 2.1279, 2.1854, 2.2518, 2.3441, 2.4008]
    
    
    

    def f(x):
        func = math.sqrt(math.cos(x**2) + x)
        return func

    n = len(x)
    k = 2 #ordem da derivada -> atenção aqui

    coeffs = dif_fin(x,x0,k)
    print(aprox(coeffs, f, x))

    
    