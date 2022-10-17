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
    return a*(x/(x+b))


def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp


if __name__ == '__main__':

    
    x = [1.3931, 1.501, 2.3098, 2.676, 3.1453, 3.3841, 4.1427, 4.3478, 4.8253, 5.3264, 5.8247, 5.9798, 6.8292, 7.0163, 7.7325, 7.8579, 8.4535, 8.7881, 9.3487, 9.7129, 10.2933, 10.7863, 11.3585, 11.7611, 12.2235, 12.7342, 12.8364, 13.4511, 14.0605, 14.128, 14.9197, 15.2182, 15.8016, 16.2076, 16.4507, 17.2757, 17.2879, 18.0572, 18.4982, 18.8996, 19.1578, 19.6298]
    y = [1.1027, 1.1492, 1.524, 1.6857, 1.8433, 1.9025, 2.138, 2.1637, 2.2643, 2.3568, 2.4602, 2.4446, 2.602, 2.6098, 2.6677, 2.687, 2.8049, 2.786, 2.8948, 2.8784, 2.9602, 2.9426, 2.9994, 3.0035, 3.0618, 3.0816, 3.1074, 3.1407, 3.1428, 3.156, 3.2109, 3.2237, 3.2602, 3.1388, 3.2265, 3.2687, 3.288, 3.2955, 3.2902, 3.3425, 3.3115, 3.3334]
    values = [4.8362, 9.2503, 10.8424, 13.5747, 18.867]

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

    a0, a1 = best_poly(x_, y_, grau)

    a = 1/a0

    b = a*a1


    #print('Coeficientes da reta')
    #print(f'{a0 = } e {a1 = }')

    #print('Coeficientes da potencia')
    print(a,',',b,',')

    p = build_func(a, b)

    def q(x):
        return p(x+k2) - k1

    for value in values:
        print(q(value),',')

