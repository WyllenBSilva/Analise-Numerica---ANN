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

    
    x = [0.5131, 1.5117, 2.5347, 3.0368, 4.094, 4.9664, 5.5786, 6.0302, 7.4385, 7.5466, 8.6047, 9.7055]
    y = [1.4618, 2.8289, 3.1579, 3.1393, 2.6991, 2.3249, 2.0502, 1.859, 1.2949, 1.2638, 0.976, 0.7269]
    values = [4.5672, 6.2104, 9.4731]
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

