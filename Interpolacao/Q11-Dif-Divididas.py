def dif_div(x, y):
    num = len(x)
    Y = [yi for yi in y]
    coefs = [y[0]]
    for j in range(num -1):
        for i in range(num - 1 - j):
            numerador = Y[i + 1] - Y[i]
            denominador = x[i + 1 + j] - x[i]
            div = numerador / denominador
            Y[i] = div
        coefs.append(Y[0])
    return coefs

def poly(t, x, coefs):
    val = 0
    num = len(coefs)
    for i in range(num):
        prod = 1
        for j in range(i):
            prod *= (t - x[j])
        val += coefs[i] * prod
    return val

def build_func(x, coefs):
    def temp(t):
        return poly(t, x, coefs)
    return temp


if __name__ == '__main__':

    #ex11
    #x = [0.776, 1.343, 2.199]
    #y = [0.884, 0.849, 0.54]

    #ex12
    #x = [1.727, 2.314, 2.573, 3.057, 3.588, 4.413, 4.882]
    #y = [-0.933, -0.893, -0.692, -0.16, 0.457, 0.989, 0.929]

    #ex13
    x = [0.259, 0.632, 1.171, 1.796, 2.247, 2.622, 2.949, 3.372, 4.063, 4.448, 4.814, 5.502, 5.728, 6.119, 6.647]
    y = [4.902, 4.478, 3.643, 2.816, 2.381, 2.133, 2.019, 2.026, 2.395, 2.739, 3.101, 3.71, 3.85, 3.987, 3.935]
    coefs = dif_div(x, y)

    #polinomio interpolador da lista de pontos
    p = build_func(x, coefs)

    print(coefs)