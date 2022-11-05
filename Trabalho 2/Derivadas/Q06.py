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


    x0 = -2.2892
    x = [-2.5158, -2.4018, -2.3538, -2.2571, -2.2394, -2.1748, -2.0556]
   

    def f(x):
        func = math.sin(x)**4 - 4*math.sin(x)**2 + math.cos(x**2) + math.exp(-x**2) + 5
        return func

    n = len(x)
    k = 3 #ordem da derivada -> atenção aqui

    coeffs = dif_fin(x,x0,k)
    print(aprox(coeffs, f, x))

    
    