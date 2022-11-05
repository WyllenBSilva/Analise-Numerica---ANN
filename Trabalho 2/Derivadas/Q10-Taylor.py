import numpy as np
import math

# x0 = ponto onde a função será derivada
# x = lista de coordenadas na proximidade de x0
# y = cálculo da função em todos os pontos x
# k = ordem da derivada

def coeffs_dif_fin(x0, x, k):
    n = len(x)
    A, B = [[1]* n], [0]
    for i in range(1, n):
        # construção da matriz A
        row_i = [xi ** i for xi in x]
        A.append(row_i)
        # construção da matriz B
        if i < k:
            B.append(0)
        elif i == k:
            B.append(math.factorial(k))
        else:
            numer = math.factorial(i)
            denom = math.factorial(i - k)
            el = (numer / denom) * x0 ** (i - k)
            B.append(el)
    return np.linalg.solve(A, B)
        
def dif_fin(coeffs, y):
    return sum(ci * yi for ci, yi in zip(coeffs, y))
        

if __name__ == '__main__':


    
    values = [-1.1714, -1.1662, -1.0352, -0.876]
    
   

    # exemplo 1:
    def f(x):
        func = math.log(2 + math.cos(math.exp(-x)))
        return func
        
    def p(xp):
        x0 = -0.9675
        order = 4
        x = [-1.1983, -1.128, -1.0396, -1.0239, -0.9461, -0.8724, -0.783, -0.7447]
        n = len(x) # numero de pontos igualmente espaçados
        # queremos pontos no intervalo [x0-e, x0+e]
        # ao diminuir o epsilon (e) os pontos são cada vez mais próximos
        e = 0.001


        y = [f(xi) for xi in x]

        #vai ate 3 nas funcoes abaixo pois order = 3.
        
        coeffs = coeffs_dif_fin(x0, x, 1)
        f_1 = dif_fin(coeffs, y)
        
        coeffs = coeffs_dif_fin(x0, x, 2)
        f_2 = dif_fin(coeffs, y)
        
        coeffs = coeffs_dif_fin(x0, x, 3)
        f_3 = dif_fin(coeffs, y)

        coeffs = coeffs_dif_fin(x0, x, 4)
        f_4 = dif_fin(coeffs, y)

        return f(x0) + f_1*(xp - x0) + (f_2/2)*((xp - x0)**2) + (f_3/6)*((xp - x0)**3)  + (f_4/math.factorial(4))*((xp - x0)**4)
    
    




    for vi in values:
        px = p(vi)
        print(px,',')
        fx_menos_px = (np.abs(f(vi) - p(vi)))
        print(fx_menos_px,',')

    