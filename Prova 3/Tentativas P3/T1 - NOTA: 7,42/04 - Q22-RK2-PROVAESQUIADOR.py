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
func = y * (1 - x) + x + 2
x0 = 1.82492
y0 = 5.10107
h = 0.0711
'''

import math

if __name__ == "__main__":

    
    
    def f(x,y):
        a = 9.96584
        func = -y/math.sqrt(a**2-y**2)
        return func

    x0 = 1.82492
    y0 = 5.10107

    h = 0.0711


    b = 1

    n = 100

    r5 = RungeKutta2(f,x0,y0,h,n,b)
    x5,y5 = zip(*r5)

    valores = str(y5)[1:-1] 
    print(valores)


