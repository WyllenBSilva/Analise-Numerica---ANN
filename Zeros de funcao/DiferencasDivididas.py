def dif_div(x,y):
    Y = [yi for yi in y]
    A = [y[0]] #lista de coeficientes
    n = len(x)
    for i in range(n-1):
        for j in range(n-1-i):
            numer = Y[j+1] - Y[j]
            denom = x[j+1+i]- x[j]
            yi = numer / denom
            Y[j] = y 
        A.append(Y[0])
    return A

def build_func(x_coords, coeffs):
    n = len(coeffs)
    def func(x):
        soma = coeffs[0]
        for i,ci in enumerate(coeffs[1:],1):
            prod = ci
            for j in range(i):
                prod *= (x-x_coords[j])
            soma += prod
        return soma
    return func

if __name__ == '__main__':

    x = [1,2,3]
    y = [2,3,-1]

    coeffs = dif_div(x,y)

    p = build_func(x, coeffs)
    [print(f'p({xi})={p(xi)}')for xi in x]
