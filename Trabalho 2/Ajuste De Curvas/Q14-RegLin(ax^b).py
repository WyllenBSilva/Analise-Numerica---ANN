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
    x = [0.6616, 0.9135, 1.0255, 1.3174, 1.3884, 1.7065, 1.9294, 2.1325, 2.3138, 2.4247, 2.7198, 2.8302]
    y = [0.4931, 0.295, 0.4357, 1.2726, 2.1582, 4.3968, 5.5809, 6.5571, 10.7287, 12.0663, 18.7425, 20.0824]
    values = [0.7474, 2.1727, 2.3518]
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

