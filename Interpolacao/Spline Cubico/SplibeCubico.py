import numpy as np


def spline(x, y):
    n = len(x)
    a = {k: v for k, v in enumerate(y)}
    h = {k: x[k + 1] - x[k] for k in range(n - 1)}

    A = [[1] + [0] * (n - 1)]
    for i in range(1, n - 1):
        row = [0] * n
        row[i - 1] = h[i - 1]
        row[i] = 2 * (h[i - 1] + h[i])
        row[i + 1] = h[i]
        A.append(row)
    A.append([0] * (n - 1) + [1])

    B = [0]
    for k in range(1, n - 1):
        row = 3 * (a[k + 1] - a[k]) / h[k] - 3 * (a[k] - a[k - 1]) / h[k - 1]
        B.append(row)
    B.append(0)

    c = dict(zip(range(n), np.linalg.solve(A, B)))

    b = {}
    d = {}
    for k in range(n - 1):
        b[k] = (1 / h[k]) * (a[k + 1] - a[k]) - (h[k] / 3) * (2 * c[k] + c[k + 1])
        d[k] = (c[k + 1] - c[k]) / (3 * h[k])

    s = {}
    for k in range(n - 1):
        print(f'Equation {k}:')
        print(f'a[{k}] = {a[k]}')
        print(f'b[{k}] = {b[k]}')
        print(f'c[{k}] = {c[k]}')
        print(f'd[{k}] = {d[k]}')
        eq = f'{a[k]}{b[k]:+}*(x{-x[k]:+}){c[k]:+}*(x{-x[k]:+})**2{d[k]:+}*(x{-x[k]:+})**3'
        s[k] = {'eq': eq, 'domain': [x[k], x[k + 1]]}

    return s

#ex15
#x = [-3.176, -0.56, 0.415, 2.611]
#y = [3.133, 1.527, 1.564, 2.651]

#ex16
#x = [1.957, 2.178, 2.887, 3.666, 4.072, 4.425, 5.197]
#y = [1.84, 3.319, 4.953, 5.566, 2.822, 3.463, 2.491]

#ex17
x = [0.293, 0.766, 1.398, 2.09, 2.727, 3.169, 3.61, 4.389, 4.92, 5.52, 6.069, 6.657]
y = [4.934, 5.098, 3.826, 3.455, 2.931, 2.585, 2.386, 3.482, 3.469, 4.204, 4.694, 4.013]
z = []

for xi, yi in z:
    x.append(xi)
    y.append(yi)

eqs = spline(x, y)

#for eq in eqs.values():
    #print(eq)


def s(x):
    for key, value in eqs.items():
        if value['domain'][0] <= x <= value['domain'][1]:
            return eval(value['eq'])