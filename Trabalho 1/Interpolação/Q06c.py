import numpy as np


def f(x):
    return (np.cos(x)**3)+(2*np.cos(x)**2)+1


def poly(x, y):
    n = len(x) - 1
    A = []
    for xi in x:
        row = [1]
        for j in range(1, n + 1):
            row.append(xi**j)
        A.append(row)
    return np.linalg.solve(A, y)


def p(x, coefs):
    first = coefs[0]
    return first + sum([ai*x**j for j, ai in enumerate(coefs[1:], 1)])


if __name__ == '__main__':
    x = [-2.467, -2.059, -1.183, -0.083, 0.717, 1.772, 2.249, 3.35, 3.831]
    y = []

    for i in x:
        y.append(f(i))

    np.set_printoptions(suppress=True)
    coefs = poly(x, y)
    print(coefs)

print(abs(f(-1.672) - p(-1.672, coefs))) #values = [-1.672, -1.645, 1.667, 3.508, 4.327]
print(abs(f(-1.645) - p(-1.645, coefs)))
print(abs(f(1.667) - p(1.667, coefs)))
print(abs(f(3.508) - p(3.508, coefs)))
print(abs(f(4.327) - p( 4.327, coefs)))#pontos