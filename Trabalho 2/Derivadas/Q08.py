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


    x0 = 3.53
    x = [3.2812, 3.3395, 3.36, 3.4088, 3.4281, 3.473, 3.5073, 3.5195, 3.5766, 3.609, 3.6199, 3.6684, 3.7019, 3.7385, 3.7541]
    

    def f(x):
        func = x**2 * math.exp(-x) * math.cos(x) + 1
        return func

    n = len(x)
    k = 5 #ordem da derivada -> atenção aqui

    coeffs = dif_fin(x,x0,k)
    print(aprox(coeffs, f, x))

    
    