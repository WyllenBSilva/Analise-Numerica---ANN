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

def f(a0,a1,a2,x):
    return a0+a1*x+a2*math.pow(x,2) #mudar se necessario

if __name__ == '__main__':
    x = [0.0011, 0.3135, 0.679, 0.8574, 1.3569, 1.5879, 1.7472, 2.1591, 2.4073, 2.7294, 3.0445, 3.3013, 3.5679, 3.6502, 4.0946, 4.188, 4.6261, 4.8888, 5.167, 5.2899, 5.6365, 5.8385, 6.2759, 6.4486, 6.884, 7.057, 7.3195, 7.6857, 7.9625, 8.3287, 8.4034, 8.7078, 8.9183, 9.2515, 9.6312, 9.723]
    y = [6.1769, 5.9897, 5.7531, 5.5791, 5.2793, 5.1191, 5.0699, 4.8178, 4.6689, 4.7884, 4.4518, 4.3125, 4.1262, 4.2126, 4.1833, 4.2186, 4.0745, 3.8468, 3.9946, 3.988, 4.0258, 3.9366, 3.9983, 3.977, 3.8728, 4.3031, 4.0316, 4.279, 4.3566, 4.467, 4.5063, 4.609, 4.7031, 4.898, 5.0, 5.1577]
    values = [3.9188, 6.2444, 7.2431, 8.6524, 9.5688]
    z = []

    a0, a1, a2 = best_poly(x, y, 2) #2 é o grau da parabola
    
    print(a0, ',', a1,',',a2,',') #cuidado com a quantidade de variaveis, se é 1, 2, 3...

    for i in x:
        z.append(f(a0,a1,a2, i))

    np.set_printoptions(suppress=True)
    coefs = poly(x, z)

    for i in values:
        print(p(i,coefs),',')
