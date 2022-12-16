def RungeKutta2(f,x0,y0,h,n,b:int=1):
    
    a = 1 - b
    p = 1 / ( 2 * b)
    q = p
    for k in range(n):
        m1 = f(x0,y0)
        m2 = f(x0 + p * h,y0 + q * h * m1)
        y0 = y0 + (a * m1 + b * m2) * h
        x0 += h
        yield[x0,y0]


''''
Se P0=(x0,y0), com x0=1.95268 e y0=5.85672, denota a posição inicial do esquiador. Use o método de Euler para estimar a posição do esquiador nos pontos xk=x0+kh, onde k=1,2,…,100. Suponha que a=8.45655 e use h=0.17956.
'''

import math

if __name__ == "__main__":

    
    
    def f(x,y):
        a = 8.45655  #valor de a
        func = -y/math.sqrt(a**2-y**2)
        return func

    x0 = 1.95268
    y0 = 5.85672

    h = 0.17956


    b = 1

    n = 100

    r5 = RungeKutta2(f,x0,y0,h,n,b)
    x5,y5 = zip(*r5)

    valores = str(y5)[1:-1] 
    print(valores)


