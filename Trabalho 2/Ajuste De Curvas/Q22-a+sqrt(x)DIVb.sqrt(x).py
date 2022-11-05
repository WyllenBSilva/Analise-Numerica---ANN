import numpy as np

#BEST_POLY

#FUNC EQUIVALENTE
# y = ((a + sqrt(x)/b sqrt (x))^2
# sqrt( y ) = 1/b + a/b * 1/sqrt( x )

"""Um pesquisador relatou os dados tabulados a seguir.
Sabe-se que tais dados podem ser modelados pela seguinte equação:
    y=(a+√x/√x * b)^2
"""
def best_poly(x, y, grau=1):
    k = grau + 1
    A = [[0 for _ in range(k)] for _ in range(k)]
    B = [sum(y)]
    n = len(x)
    cache = {}
    for i in range(k):
        for j in range(k):
            p=i+j
            if p == 0:
                A[0][0] = n
                continue
            if p not in cache:
                cache[p] = sum([xi ** p for xi in x])
            A[i][j] = cache[p]
        if i > 0:
            B.append(sum([yi * xi ** i for xi, yi in zip(x, y)]))
    return np.linalg.solve(A, B)


def poly(x, coefs):
    s = coefs[0]
    for i, ci in enumerate(coefs[1:], 1):
        s += ci * x ** i
    return s

def build_func(coefs):
    def temp(x):
        return poly(x, coefs)
    return temp


def modelo(x):
    a, b = -10, 10
    erro = a + (b - a) * np.random.random()
    return 2 + 2.34 * x - 1.86 * x ** 2 - 3.21 * x ** 3 + erro


if __name__ == '__main__':
    

    x = [0.6617, 1.6259, 2.2288, 3.1092, 4.2057, 4.922, 5.9273, 6.2918, 6.8523, 7.8517, 9.1515, 9.753]
    y = [12.9853, 6.3406, 4.9821, 3.8729, 3.1897, 2.8952, 2.551, 2.4457, 2.3497, 2.0777, 1.9404, 1.8979]
    values = [5.1078, 7.2008, 9.1475]

    y_ = np.sqrt(y)
    
    x_ = 1/np.sqrt(x)

    grau = 1

    coefs = best_poly(x_, y_, grau)

    grau = 1

    a0, a1 = best_poly(x_, y_, grau)

    b = 1/a0
    a = a1 * b

    p = build_func(coefs)

    n = len(coefs)

    '''for xi in range(n):
        print(f'a{xi} = [{coefs[xi]}]')'''

    print(f'a = {a} b = {b}')

    n = len(values)
    for xi in range(n):
        print(f'{(a0 + a1 * 1/np.sqrt(values[xi]))**2}, ')

