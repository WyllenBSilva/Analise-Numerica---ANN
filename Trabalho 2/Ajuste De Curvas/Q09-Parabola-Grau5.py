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

def f(a0,a1,a2,a3,a4,a5,x):
    #a0+a1x+a2x2+a3x3
    return a0+a1*x+a2*x**2+a3*x**3+a4*x**4+a5*x**5

if __name__ == '__main__':
    x = [-3.9852, -3.4355, -3.0512, -2.7543, -1.7891, -1.2552, -1.0326, -0.539, 0.3301, 0.673, 1.6474, 2.0421, 2.4457, 2.8992, 3.6627, 4.1967]
    y = [-0.9873, 1.5381, 1.1682, 1.1059, 0.2716, -0.4915, -0.2207, -0.3294, 0.8095, 0.6878, -0.0619, -0.0466, -0.3919, -1.3313, -0.8518, -0.5878]
    values = [-3.967, 1.0152, 3.9644]
    z = []

    a0, a1, a2, a3, a4, a5 = best_poly(x, y, 5) #3 é o grau da parabola
    
    print(a0,',', a1,',',a2,',',a3,',',a4,',',a5,',') #cuidado com a quantidade de variaveis, se é a1, a2, a3...

    for i in x:
        z.append(f(a0,a1,a2,a3,a4,a5, i)) #nao esqueça de colocar aqui tb

    np.set_printoptions(suppress=True)
    coefs = poly(x, z)

    for i in values:
        print(p(i,coefs),',')
