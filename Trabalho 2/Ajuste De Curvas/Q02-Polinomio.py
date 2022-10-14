from ctypes import sizeof
import numpy as np

def linear(x,y):
    n = len(x)
    sum_x = sum(x)
    sum_x2 = sum(xi**2 for xi in x)
    A = [
        [n,sum_x],
        [sum_x,sum_x2]
    ]
    sum_y = sum(y)
    sum_yx = sum(yi*xi for yi,xi in zip(y,x))
    B = [
        sum_y,
        sum_yx
    ]
    return np.linalg.solve(A,B)

def f(a0,a1,x):
    return a0 + a1 * x #mudar se necessario


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
    x = [0.0695, 0.3154, 0.9313, 0.9663, 1.3742, 1.5811, 1.8752, 2.4716, 2.5807, 2.8403, 3.3183, 3.582, 3.8562, 4.1893, 4.5261, 4.7594, 5.2687, 5.5222, 5.9185, 6.0409, 6.4278, 6.7025, 6.9696, 7.2064, 7.6733, 7.8324, 8.254, 8.6202, 8.9519, 9.1447, 9.6703, 9.8414]
    y = [4.6295, 5.4416, 6.8186, 6.8975, 8.0225, 8.5745, 9.5037, 10.0016, 10.8146, 11.5835, 12.6776, 13.3533, 14.1312, 14.8836, 15.7436, 16.2999, 17.431, 18.0236, 18.9784, 19.0062, 20.2239, 20.8906, 21.6626, 22.0296, 23.2159, 23.7898, 24.7467, 25.5829, 26.6799, 26.9858, 28.1032, 28.6069]
    values = [1.3615, 4.1132, 4.1818, 7.5934, 7.6574]
    z = []

    a0, a1 = linear(x,y)
    
    print(a0, ',', a1,',')

    for i in x:
        z.append(f(a0, a1, i))

    np.set_printoptions(suppress=True)
    coefs = poly(x, z)

    for i in values:
        print(p(i,coefs),',')
