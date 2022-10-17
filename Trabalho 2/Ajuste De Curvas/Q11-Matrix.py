from ntpath import join
from traceback import print_last
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

def matriz_Coeffs(x,y,k):
    n = len(x)
    if n <= k:
        raise ValueError('O número de pontos deve ser maior que k (o grau do polinônmio)')

    somas = {}
    somas[0] = n
    for n in range(1, 2*k + 1):
        somas[n] = sum(xi ** n for xi in x)
    A = []
    for i in range (k + 1):
        row = []
        for j in range(k + 1):
            row.append(somas[i + j])
        A.append(row)
    return A

def matrix_TermosIndepents(x,y,k):
    n = len(x)
    if n <= k:
        raise ValueError('O número de pontos deve ser maior que k (o grau do polinônmio)')

    B = []
    for i in range (k + 1):
        if i == 0:
            B.append(sum(y))
        else:
            B.append(sum(xi ** i * yi for xi, yi in zip(x,y)))
    return B

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

def f(a0,a1,a2,x):
    return a0+a1*x+a2*math.pow(x,2) #mudar se necessario

if __name__ == '__main__':
    x = [0.433, 0.9193, 2.3771, 2.607, 3.7189, 4.762, 5.591, 6.5247, 6.7945, 8.2052, 8.5295, 9.2964]
    y = [4.4885, 4.1141, 3.6313, 3.6013, 3.3272, 3.4495, 3.6049, 3.9019, 4.0502, 4.8774, 5.0229, 5.847]
    values = [1.4417, 5.2905, 7.5545]
    z = []

    a0, a1, a2 = best_poly(x, y, 2) #2 é o grau da parabola
    
    #print(a0, ',', a1,',',a2,',') #cuidado com a quantidade de variaveis, se é 1, 2, 3...

    for i in x:
        z.append(f(a0,a1,a2, i))

    np.set_printoptions(suppress=True)
    coefs = poly(x, z)

    #
    print('\**nRetire os colchetes somente e coloque virgulas quando necessario**')
    A = matriz_Coeffs(x,y,2)
    print(*A,sep=','+'\n')

    print(a0, ',', a1,',',a2,',')

    B = matrix_TermosIndepents(x,y,2)
    print(*B,sep=', ')

    for i in values:
        print(p(i,coefs),',')
