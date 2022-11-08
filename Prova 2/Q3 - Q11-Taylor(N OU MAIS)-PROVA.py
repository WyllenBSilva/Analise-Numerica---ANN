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

    #valores a alterar: Values, Func (em def f(x)), x0,order e x em (def p(x))
    
    
    values = [-1.6697, -1.4758, -1.3862]
    
    
   

    # exemplo 1:
    def f(x):
        func = x**2 * math.tan(math.sin(x / math.pi))
        return func
        
    def p(xp):

        x0 = -1.4409
        order = 5
        x = [-1.6862, -1.5934, -1.5539, -1.5094, -1.4864, -1.4198, -1.3879, -1.3057, -1.2863, -1.2295]
        

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

    