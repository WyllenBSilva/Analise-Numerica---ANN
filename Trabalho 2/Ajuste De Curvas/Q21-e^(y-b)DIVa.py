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
    return a*np.log(x)+b


def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp


if __name__ == '__main__':

    
    x = [1.2247, 1.7674, 2.5551, 3.8301, 4.0628, 5.3908, 6.1998, 6.3579, 7.0236, 8.1919, 8.7445, 9.624]
    y = [4.6723, 5.3608, 5.9631, 6.716, 6.5897, 7.2966, 7.7063, 7.6065, 7.768, 8.0036, 8.1255, 8.29]
    values = [6.1704, 8.3099, 9.004]
    if min(y) <= 0:
        k1 = abs(min(y)) + 1
    else:
        k1 = 0

    if min(x) <= 0:
        k2 = abs(min(x)) + 1
    else:
        k2 = 0

    yt = [yi + k1 for yi in y]

    y_ = y #testar com y_ = y tambem

    #xt = [xi + k2 for xi in x]

    x_ = np.log(x)
    grau = 1

    a0, a1 = best_poly(x_, y_, grau)

    a = a1
    b = a0


    #print('Coeficientes da reta')
    #print(f'{a0 = } e {a1 = }')

    #print('Coeficientes da potencia')
    print(a,',',b,',')

    p = build_func(a, b)

    def q(x):
        return p(x+k2) - k1

    for value in values:
        print(q(value),',')

