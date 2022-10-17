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

    
    x = [1.0893, 3.3447, 4.6864, 5.9195, 8.4915, 9.9141, 10.6629, 13.0544, 14.2161, 15.418, 18.33, 19.4522]
    y = [0.9357, 2.015, 2.3256, 2.5211, 2.8476, 2.966, 3.0485, 3.1135, 3.2836, 3.3365, 3.4271, 3.4784]
    values = [8.4831, 12.6492, 18.7524]

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

