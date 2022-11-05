import numpy as np

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
    return a*x*np.exp(b*x)


def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp


if __name__ == '__main__':

    
    x = [0.2116, 0.4603, 0.6601, 0.8854, 1.1589, 1.5224, 1.7578, 1.8392, 2.15, 2.3032, 2.5219, 2.8257, 3.0309, 3.394, 3.6477, 3.8523, 4.0709, 4.3492, 4.4708, 4.6169, 4.9806, 5.2566, 5.5281, 5.6715, 5.8088, 6.1799, 6.2663, 6.6869, 6.8458, 6.9885, 7.3682, 7.5215, 7.7537, 8.0471, 8.1483, 8.4846, 8.638, 8.9251, 9.1622, 9.3026, 9.6903, 9.8124]
    y = [0.8997, 1.8517, 2.4002, 3.0318, 3.6744, 4.3935, 4.7602, 4.9155, 5.3761, 5.4653, 5.75, 5.8528, 5.982, 6.0752, 6.2352, 6.2074, 6.2072, 6.1591, 6.0907, 6.0608, 5.9998, 5.937, 5.9484, 5.7396, 5.6409, 5.4614, 5.4127, 5.1878, 5.2032, 5.051, 4.8117, 4.7518, 4.6409, 4.5115, 4.3745, 4.3483, 4.1096, 4.1284, 3.8415, 3.7529, 3.5184, 3.5197]
    values = [2.8938, 3.4047, 5.5472, 6.9923, 8.7344]
    if min(y) <= 0:
        k1 = abs(min(y)) + 1
    else:
        k1 = 0

    if min(x) <= 0:
        k2 = abs(min(x)) + 1
    else:
        k2 = 0

    yt = [yi + k1 for yi in y]

    y_ = np.log(y) - np.log(x)

    #xt = [xi + k2 for xi in x]

    x_ = x
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

