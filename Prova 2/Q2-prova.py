import numpy as np

#BEST_POLY

# c0* (1/sqrt(1+2*k*c0²*t)
#FUNC EQUIVALENTE
# 1/y² = 1/a² + 2bx

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





if __name__ == '__main__':
    
    x = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7]
    y = [1.36103, 0.97959, 0.80549, 0.6998, 0.62718, 0.57335, 0.53167, 0.49569, 0.4693, 0.4457, 0.42524, 0.40654, 0.39137, 0.37675]
    values = [1.2, 5.4, 5.7]    

    y_ = 1/np.power(y, 2)
    
    x_ = x

    grau = 1

    coefs = best_poly(x_, y_, grau)

    grau = 1

    a0, a1 = best_poly(x_, y_, grau)

    a = 1/np.sqrt(a0)
    b = a1/2

    p = build_func(coefs)

    n = len(coefs)

    for xi in range(n):
        print(f'a{xi} = [{coefs[xi]}]')

    print(f'a = {a} b = {b}')

    n = len(values)
    for xi in range(n):
        print(f'y(x{xi+1}) = {a/(np.sqrt(1+2*b*(a**2)*values[xi]))}')
