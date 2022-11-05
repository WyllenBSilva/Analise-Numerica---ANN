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


    x0 = 1.1179
    x = [0.9129, 0.9679, 0.9935, 1.0696, 1.133, 1.1557, 1.2057, 1.3113, 1.3489]
    

    def f(x):
        func = math.cos(math.exp(-x**2)) + math.sin(x**2 / 2)
        return func

    n = len(x)
    k = 1 #ordem da derivada

    coeffs = dif_fin(x,x0,k)
    print(aprox(coeffs, f, x))

    
    