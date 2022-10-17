import numpy as np

#ae^(bx)

def best_poly(x, y, grau = 1):
    k = grau + 1
    A = [[0 for _ in range(k)] for _ in range(k)]
    B = [sum(y)]
    n = len(x)
    cache = {}
    for i in range(k):
        for j in range(k):
            p = i + j
            if (p == 0):
                A[0][0] = n
                continue
            if p not in cache:
                cache[p] = sum([xi ** p for xi in x])
            A[i][j] = cache[p]
        if i > 0:
            B.append(sum([yi * xi ** i for xi, yi in zip(x, y)]))
    return np.linalg.solve(A, B)

def poly(x, a, b):
    return a * np.exp(b * x)

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp

if __name__ == '__main__':

    x = [0.0209, 0.2538, 0.3847, 0.5088, 0.8271, 0.8367, 1.0595, 1.3239, 1.4638, 1.6334, 1.7378, 1.8948]
    y = [4.6461, 6.3547, 6.8234, 10.4571, 20.4069, 17.8082, 28.4532, 43.1168, 55.8082, 75.8218, 89.9848, 120.8411]
    values = [0.1573, 0.417, 1.0672]
    y_ = np.log(y)

    grau = 1

    a0, a1 = best_poly(x, y_, grau)

    #print(f'{a0 = } e {a1 = }')

    a = np.exp(a0)
    b = a1

    #print(f'{a = } e {b = }')
    print(a,',',b,',')

    p = build_func(a, b)
    
    for xi_v in values:
        print(p(xi_v),',')
