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


    
    
    
    values = [0.6793, 0.7481, 0.8136, 0.8895, 0.9623]
    
   

    # exemplo 1:
    def f(x):
        func = x**2 * math.cos(x - 1) * math.exp(-3 * x ** 2)
        return func
        
    def p(xp):

        x0 = 0.866
        order = 5
        x = [0.6639, 0.7073, 0.7171, 0.7797, 0.8464, 0.9027, 0.9296, 1.0015, 1.0224, 1.0985]
        

        soma = f(x0)
        y = [f(xi) for xi in x]

        #vai ate 3 nas funcoes abaixo pois order = 3.

        for n in range(1,order+1):
            
            coeffs = coeffs_dif_fin(x0, x, n)
            fn = dif_fin(coeffs, y)
            
            soma = soma + ((fn/math.factorial(n))*(xp-x0)**n)
        
        return soma

    
    




    for vi in values:
        px = p(vi)
        print(px,',')
        fx_menos_px = (np.abs(f(vi) - p(vi)))
        print(fx_menos_px,',')

    