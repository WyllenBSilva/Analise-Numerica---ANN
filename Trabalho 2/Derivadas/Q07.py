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


    x0 = 3.2929
    x = [3.0878, 3.1393, 3.2207, 3.2679, 3.3217, 3.3923, 3.4271, 3.5398]

    def f(x):
        func = math.sin(math.sqrt(math.pi + x**2))
        return func

    n = len(x)
    k = 4 #ordem da derivada -> atenção aqui

    coeffs = dif_fin(x,x0,k)
    print(aprox(coeffs, f, x))

    
    