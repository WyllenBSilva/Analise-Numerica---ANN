import numpy as np
import math


'''
Encontre os coeficientes a e b da função taxa de crescimento da saturação y=a(x/(x+b) que melhor se aproxima da seguinte lista de 12 pontos
(2.106,0.8735)...
'''

def best_line(x, y, grau=1):
    n = len(x)
    # soma das coordenadas x
    sum_x = sum(x)
    # soma das coordenadas x**2
    sum_x2 = sum(xi ** 2 for xi in x)
    # soma das coordenadas y
    sum_y = sum(y)
    #soma das coordenadas x*y
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))

    # Matriz dos coeficientes
    A = [[n, sum_x], [sum_x, sum_x2]]
    # Matriz dos termos independentes
    B = [sum_y, sum_xy]

    return np.linalg.solve(A, B)

def poly(x, a, b):
    return a * (x/(x+b))
    # funcaomath.pow(x,b)

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp

if __name__ == '__main__':

    x = [1.1502, 1.4908, 2.0736, 2.6124, 2.826, 3.1772, 3.5134, 3.9757, 4.5646, 4.6855, 5.2474, 5.515, 6.1246, 6.3269, 6.714, 7.1778, 7.7095, 8.2633, 8.3302, 8.9255, 9.4322, 9.8295, 10.1777, 10.3592, 10.791, 11.3469, 11.8569, 12.102, 12.6276, 12.9174, 13.3296, 13.8278, 14.2933, 14.5635, 14.9548, 15.32, 15.7382, 16.1571, 16.4257, 17.033, 17.4104, 17.8281, 18.2308, 18.6314, 18.9568, 19.4802, 19.7839]
    y = [0.7733, 0.9315, 1.1025, 1.2767, 1.3258, 1.4245, 1.4466, 1.5588, 1.6504, 1.6493, 1.6967, 1.8049, 1.8309, 1.8341, 1.8531, 1.8955, 1.8766, 1.936, 1.9493, 2.0671, 1.9953, 1.9448, 2.0315, 2.0459, 2.0709, 2.0446, 2.1279, 2.1416, 2.1191, 2.1642, 2.1362, 2.1578, 2.1475, 2.1978, 2.1858, 2.1861, 2.2039, 2.2422, 2.2359, 2.2458, 2.2719, 2.1672, 2.2387, 2.2585, 2.2729, 2.2883, 2.2773]
    values = [15.3395, 16.7929, 17.831, 19.5623]

    if min(y) <= 0:
        k1 = abs(min(y)) + 1
    else:
        k1 = 0

    if min(x) <= 0:
        k2 = abs(min(x)) + 1
    else:
        k2 = 0

    yt = [yi + k1 for yi in y]

    y_ = (np.divide(1,y))

    xt = [xi + k2 for xi in x]

    x_ = np.divide(1,x)
    grau = 1

    a0, a1 = best_line(x_, y_, grau)

    a = 1/a0

    b = a1/a0
    print('Coeficientes da reta')
    print(f'{a0 = } e {a1 = }')

    print('Coeficientes')
    print(f'{a = } e {b = }')

    p = build_func(a, b)

    def q(x):
        return p(x+k2) - k1

    px = [p(vi) for vi in values]
    print(f'{px = }')
