import numpy as np
import math

# k = kmax*C²/cs+C²

"""Um pesquisador relatou os dados tabulados a seguir de um experimento realizado 
para determinar a taxa de crescimento k (por dia) de bactérias como uma função da 
concentração de oxigênio c (em mg/L).
Sabe-se que tais dados podem ser modelados pela seguinte equação:
        k = kmax*C²/cs+C²
onde cs e kmax são parâmetros. Use uma transformação para linearizar essa equação. 
A seguir, use regressão linear para encontrar os valores de cs e kmax e prever a taxa de 
crescimento para as seguintes concentrações de oxigênio
    c1=5.7891mg/L , c2=8.5182mg/L  e  c3=9.2664mg/L"""

def best_line(x, y, grau=1):
    n = len(x)
    # soma das coordenadas x
    sum_x = sum(x)
    # soma das coordenadas x**2
    sum_x2 = sum(xi ** 2 for xi in x)
    # soma das coordenadas y
    sum_y = sum(y)
    #soma das coordenadas x*y
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))

    # Matriz dos coeficientes
    A = [[n, sum_x], [sum_x, sum_x2]]
    # Matriz dos termos independentes
    B = [sum_y, sum_xy]

    return np.linalg.solve(A, B)

def poly(x, a, b):
    return (a*x**2)/(b+x**2)
    # funcaomath.pow(x,b)

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp

if __name__ == '__main__':
    c = [1.8839, 2.4781, 3.6467, 4.6323, 5.4654, 5.7643, 7.084, 7.6298, 8.4114, 10.1336, 10.2125, 11.4365]
    k = [1.9477, 2.5331, 3.1226, 3.3555, 3.5388, 3.4795, 3.5791, 3.7902, 3.7887, 3.9149, 3.743, 3.8802]
    values = [7.6452, 8.7411, 9.5332]

    if min(k) <= 0:
        k1 = abs(min(k)) + 1
    else:
        k1 = 0

    if min(c) <= 0:
        k2 = abs(min(c)) + 1
    else:
        k2 = 0

    yt = [yi + k1 for yi in k]

    y_ = (np.divide(1,k))

    xt = [xi + k2 for xi in c]

    x_ = np.divide(1,(np.power(c,2)))
    grau = 1

    a0, a1 = best_line(x_, y_, grau)

    kmax = 1/a0

    cs = a1*kmax
    #print('Coeficientes da reta')
    #print(f'{a0 = } e {a1 = }')

    print('Coeficientes')
    #print(f'{kmax = } e {cs = }')
    print(kmax,',',cs,',')

    p = build_func(kmax, cs)

    def q(x):
        return p(x+k2) - k1

    for value in values:
        print(q(value),',')