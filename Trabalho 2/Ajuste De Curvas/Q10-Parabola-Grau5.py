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
    x = [-4.3667, -4.1491, -3.9237, -3.7146, -3.5437, -3.3581, -3.0962, -2.7711, -2.5384, -2.47, -2.1885, -1.8805, -1.7782, -1.5545, -1.3982, -1.1004, -0.9264, -0.7231, -0.3516, -0.3151, -0.0676, 0.2712, 0.4133, 0.624, 0.9517, 1.0021, 1.3242, 1.5794, 1.6659, 2.0829, 2.1568, 2.3697, 2.6545, 2.9304, 3.0459, 3.271, 3.5019, 3.8196, 3.9275, 4.2312, 4.3718]
    y = [-2.7837, -0.7777, 0.551, 0.8665, 1.5165, 1.2166, 1.7774, 1.2738, 0.935, -0.2866, -1.4135, 0.1159, -0.2618, -1.3719, -0.6757, -0.6439, -0.4139, -0.7811, -1.2435, -0.0272, 0.0664, 0.2956, -0.1683, 0.5539, 0.506, 0.4741, 0.7334, 0.1653, -1.1294, -1.1123, -0.5648, -0.3102, -1.0375, -1.1161, -1.0993, -1.2066, -1.6713, -1.4145, -2.2213, 1.3729, 3.3535]
    values = [-4.2173, -3.7153, -2.1551, 1.8962, 2.4019]
    z = []

    a0, a1, a2, a3, a4, a5 = best_poly(x, y, 5) #3 é o grau da parabola
    
    print(a0,',', a1,',',a2,',',a3,',',a4,',',a5,',') #cuidado com a quantidade de variaveis, se é a1, a2, a3...

    for i in x:
        z.append(f(a0,a1,a2,a3,a4,a5, i)) #nao esqueça de colocar aqui tb

    np.set_printoptions(suppress=True)
    coefs = poly(x, z)

    for i in values:
        print(p(i,coefs),',')
