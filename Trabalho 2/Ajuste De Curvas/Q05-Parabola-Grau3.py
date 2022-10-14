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
    x = [-4.9611, -3.2981, -2.6794, -1.9106, -1.2767, -0.2322, 0.842, 1.3694, 2.4439, 3.5773, 4.8809]
    y = [2.0753, 4.6269, 5.1638, 4.8583, 5.6926, 5.6689, 3.5598, 2.8997, 2.7038, 3.7635, 5.9451]
    values = [-1.9842, 0.0155, 0.5713]
    z = []

    a0, a1, a2, a3 = best_poly(x, y, 3) #3 é o grau da parabola
    
    print(a0,',', a1,',',a2,',',a3,',') #cuidado com a quantidade de variaveis, se é 1, 2, 3...

    for i in x:
        z.append(f(a0,a1,a2,a3, i))

    np.set_printoptions(suppress=True)
    coefs = poly(x, z)

    for i in values:
        print(p(i,coefs),',')
