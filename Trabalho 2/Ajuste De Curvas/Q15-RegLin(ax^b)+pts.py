import numpy as np
'''
Encontre os coeficientes a e b da função potência y=ax^b que melhor se aproxima da seguinte lista de 12 pontos
'''


def best_poly(x, y, grau=1):
    k = grau + 1
    A = [[0 for _ in range(k)] for _ in range(k)]
    B = [sum(y)]
    n = len(x)
    cache = {}
    for i in range(k):
        for j in range(k):
            p = i + j
            if p == 0:
                A[0][0] = n
                continue
            if p not in cache:
                cache[p] = sum([xi**p for xi in x])
            A[i][j] = cache[p]
        if i > 0:
            B.append(sum([yi*xi**i for xi, yi in zip(x, y)]))
    return np.linalg.solve(A, B)


def poly(x, a, b):
    return a*x**b


def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp


if __name__ == '__main__':
    x = [0.5247, 0.5807, 0.6628, 0.7346, 0.7521, 0.8155, 0.8769, 0.9582, 0.9986, 1.0859, 1.1015, 1.1779, 1.2668, 1.2899, 1.3905, 1.4229, 1.4633, 1.5539, 1.5729, 1.6568, 1.6908, 1.7612, 1.8632, 1.8835, 1.9708, 2.0264, 2.1024, 2.1238, 2.2033, 2.2771, 2.3252, 2.3888, 2.4185, 2.4783, 2.5732, 2.6007, 2.6926, 2.7533, 2.7977, 2.8761, 2.9227, 2.9564]
    y = [0.0446, 0.0313, 0.6879, 0.9605, 1.938, 1.7876, 1.9804, 2.3403, 3.0995, 4.3019, 4.0436, 5.3123, 5.2562, 7.4477, 10.4357, 11.0088, 11.7638, 15.3175, 16.318, 19.645, 21.7305, 24.9221, 29.4332, 30.7427, 36.7191, 40.3145, 46.2796, 47.1206, 54.9522, 61.8939, 67.3143, 74.1938, 78.0945, 84.2631, 97.1331, 101.6963, 115.1193, 125.0325, 132.2007, 147.0687, 157.0526, 162.8384]
    values = [0.9109, 0.9968, 2.0402, 2.6593, 2.7623]
    if min(y) <= 0:
        k1 = abs(min(y)) + 1
    else:
        k1 = 0

    if min(x) <= 0:
        k2 = abs(min(x)) + 1
    else:
        k2 = 0

    yt = [yi + k1 for yi in y]

    y_ = np.log(yt)

    xt = [xi + k2 for xi in x]

    x_ = np.log(xt)

    grau = 1

    a0, a1 = best_poly(x_, y_, grau)

    a = np.exp(a0)

    b = a1

    #print('Coeficientes da reta')
    #print(f'{a0 = } e {a1 = }')

    #print('Coeficientes da potencia')
    print(a,',',b,',')

    p = build_func(a, b)

    def q(x):
        return p(x+k2) - k1

    for value in values:
        print(q(value),',')

