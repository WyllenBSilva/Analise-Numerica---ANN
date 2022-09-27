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
        #print(f'Equation {k}:')
        #print(f'{a[k]},')
        #print(f'{b[k]},')
        #print(f'{c[k]},')
        #print(f'{d[k]},')
        eq = f'{a[k]}{b[k]:+}*(x{-x[k]:+}){c[k]:+}*(x{-x[k]:+})**2{d[k]:+}*(x{-x[k]:+})**3'
        s[k] = {'eq': eq, 'domain': [x[k], x[k + 1]]}

    return s

#ex19-A
#x = [1.648, 2.654, 3.615, 4.495]
#y = [-0.65, 0.258, 1.331, 1.98]

#ex-19-B
#x = [0.512, 0.614, 1.142, 1.56, 1.794, 1.987, 2.578, 2.786]
#y = [0.705, 1.008, 1.264, 1.153, 0.621, 1.155, 0.616, 1.215]

#ex19-C
x = [0.29, 0.788, 1.308, 2.017, 2.405, 3.243, 3.846, 4.493, 4.844, 5.481, 6.015, 6.786]
y = [5.791, 5.144, 3.94, 3.198, 2.298, 2.701, 2.31, 2.981, 3.8, 4.645, 4.658, 4.335]
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

#ex19-A [2.668, 4.095]
#print(s(2.668))
#print(s(4.095))

#ex19-B valores = [1.386, 1.704, 2.734]
#print(s(1.386))
#print(s(1.704))
#print(s(2.734))

#ex19-C valores = [1.142, 2.408, 3.065, 3.69, 4.732]
print(s(1.142))
print(s(2.408))
print(s(3.065))
print(s(3.69))
print(s(4.732))







"""for key, value in eqs.items():
    def p(x):
        return eval(value['eq'])
    t = np.linspace(*value['domain'], 100)
    plt.plot(t, p(t), label=f'$S_{key}(x)$')
plt.scatter(x, y)
plt.legend()
plt.savefig('spline.png')"""