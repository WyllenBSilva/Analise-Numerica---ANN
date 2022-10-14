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

def f(a0,a1,a2,a3,a4,x):
    #a0+a1x+a2x2+a3x3
    return a0+a1*x+a2*x**2+a3*x**3+a4*x**4

if __name__ == '__main__':
    x = [-4.9251, -4.4389, -4.3299, -3.9438, -3.5745, -3.4781, -3.0422, -2.8761, -2.6781, -2.3852, -1.9006, -1.7828, -1.3079, -1.0834, -0.7673, -0.5116, -0.2727, 0.1717, 0.239, 0.7043, 0.8844, 1.2348, 1.5412, 1.7782, 2.0416, 2.2396, 2.6753, 2.9046, 3.3342, 3.4633, 3.776, 4.0812, 4.3276, 4.801, 4.8608, 5.1789, 5.5625, 5.8567]
    y = [-3.6898, -2.1794, -1.2388, 0.1403, 1.3657, 1.2372, 1.5251, 1.8193, 1.0592, 1.3274, 0.9001, -0.1455, -0.0379, 0.2927, -0.3557, -0.4394, -0.332, 0.0088, -1.7519, -0.1787, -0.346, -0.4014, 0.8328, 0.0394, 1.598, 1.827, 3.7726, 2.8756, 3.8788, 2.4429, 3.1259, 2.7698, 2.4657, 1.2437, 0.7291, -1.0034, -3.9583, -7.3223]
    values = [-2.6801, -0.3432, 2.5407, 3.3137, 5.117]
    z = []

    a0, a1, a2, a3, a4 = best_poly(x, y, 4) #3 é o grau da parabola
    
    print(a0,',', a1,',',a2,',',a3,',',a4,',') #cuidado com a quantidade de variaveis, se é a1, a2, a3...

    for i in x:
        z.append(f(a0,a1,a2,a3,a4, i)) #nao esqueça de colocar aqui tb

    np.set_printoptions(suppress=True)
    coefs = poly(x, z)

    for i in values:
        print(p(i,coefs),',')
