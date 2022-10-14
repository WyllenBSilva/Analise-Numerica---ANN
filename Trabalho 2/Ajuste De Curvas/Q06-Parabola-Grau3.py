import numpy as np
import math

def best_poly (x, y, k):
    n = len(x)
    if n <= k:
        raise ValueError('O número de pontos deve ser maior que k (o grau do polinônmio)')

    somas = {}
    somas[0] = n
    for n in range(1, 2*k + 1):
        somas[n] = sum(xi ** n for xi in x)
    A = []
    B = []
    for i in range (k + 1):
        row = []
        for j in range(k + 1):
            row.append(somas[i + j])
        A.append(row)
        if i == 0:
            B.append(sum(y))
        else:
            B.append(sum(xi ** i * yi for xi, yi in zip(x,y)))
    return np.linalg.solve(A, B)



def poly(x, y):
    n = len(x) - 1
    A = []
    for xi in x:
        row = [1]
        for j in range(1, n + 1):
            row.append(xi**j)
        A.append(row)
    return np.linalg.solve(A, y)


def p(x, coefs):
    first = coefs[0]
    return first + sum([ai*x**j for j, ai in enumerate(coefs[1:], 1)])

def f(a0,a1,a2,a3,x):
    #a0+a1x+a2x2+a3x3
    return a0+a1*x+a2*x**2+a3*x**3 #mudar se necessario

if __name__ == '__main__':
    x = [-4.9909, -4.6292, -4.2019, -4.0063, -3.7275, -3.3212, -2.9766, -2.8901, -2.4224, -2.0973, -1.9582, -1.5687, -1.2135, -1.0685, -0.8383, -0.5374, -0.2603, 0.1455, 0.3423, 0.6734, 0.9997, 1.3725, 1.6079, 1.9336, 2.1009, 2.5433, 2.9025, 3.2258, 3.3813, 3.5416, 3.9948, 4.3049, 4.6231, 4.9639]
    y = [3.3047, 4.5147, 4.0789, 4.6073, 4.3682, 6.0189, 5.6079, 6.6934, 5.7562, 5.7995, 5.3342, 3.3996, 4.9797, 4.286, 4.727, 4.595, 4.5647, 3.9867, 3.904, 3.5973, 3.4948, 2.9817, 3.2898, 3.1529, 2.7396, 2.7904, 2.7974, 3.2615, 3.2848, 3.4273, 3.868, 3.7733, 4.8184, 5.9081]
    values = [-4.4813, -1.9525, -1.5569, 1.5525, 4.755]
    z = []

    a0, a1, a2, a3 = best_poly(x, y, 3) #3 é o grau da parabola
    
    print(a0,',', a1,',',a2,',',a3,',') #cuidado com a quantidade de variaveis, se é a1, a2, a3...

    for i in x:
        z.append(f(a0,a1,a2,a3, i))

    np.set_printoptions(suppress=True)
    coefs = poly(x, z)

    for i in values:
        print(p(i,coefs),',')
