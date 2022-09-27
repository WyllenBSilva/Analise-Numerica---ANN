import numpy as np
#import matplotlib.pylab as plt
import math


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
        #print(f'Equation {k}:')
        print(f'{a[k]},')
        print(f'{b[k]},')
        print(f'{c[k]},')
        print(f'{d[k]},')
		#print(f'Equation {k}:')
        #print(f'a[{k}] = {a[k]}')
        #print(f'b[{k}] = {b[k]}')
        #print(f'c[{k}] = {c[k]}')
        #print(f'd[{k}] = {d[k]}')
        eq = f'{a[k]}{b[k]:+}*(x{-x[k]:+}){c[k]:+}*(x{-x[k]:+})**2{d[k]:+}*(x{-x[k]:+})**3'
        s[k] = {'eq': eq, 'domain': [x[k], x[k + 1]]}

    return s


x = [-0.976, -0.724, -0.55, -0.355, -0.201, -0.068, 0.125, 0.213, 0.437, 0.599, 0.811, 0.94]
y = []


def f(x):
    return 1.0/(1+25*x**2)


for xi in x:
    y.append(f(xi))

eqs = spline(x, y)

#for eq in eqs.values():
    #print(eq)


#def s(x):
    #for key, value in eqs.items():
       # if value['domain'][0] <= x <= value['domain'][1]:
           # return eval(value['eq'])


for key, value in eqs.items():
    def p(x):
        return eval(value['eq'])
    t = np.linspace(*value['domain'], 100)
    #plt.plot(t, p(t), label=f'$S_{key}(x)$')

#plt.scatter(x, y)
#plt.legend()
#plt.savefig('spline.png')