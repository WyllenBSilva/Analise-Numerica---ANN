import math
import numpy as np


def trapz(f, a, b, n):
    h = abs(b - a) / n
    sum_fx = 0

    for i in range(1, n):
        sum_fx += f(a + i * h)

    return (f(a) + 2 * sum_fx + f(b)) * h / 2


def coef(f,g):
    # a = -1.05973 
    # b=1.4086
    a= -1.11477
    b= 1.09286
    n = 256
    func = lambda x: (f(x) * g(x) ) 
    func2 = lambda x: g(x) * g(x)
    numer = trapz(change(func,a,b),-1,1,n)
    denom = trapz(change(func2,a,b),-1,1,n)
    
    return (numer/denom)



def change(f, a, b):
    def g(u):
        return f((b + a) / 2 + (b - a) * u / 2) * (b - a) / 2

    return g



        
if __name__ == '__main__':
    
    def f1(x): return 1
    def f2(x): return x
    def f3(x): return x**2
    def f4(x): return x**3
    
    def g1(x): 
        return f1(x)

    a_21 =  coef(f2, g1)
    print(f'{a_21},')
    
    def g2(x):
        return f2(x) - a_21*g1(x)
    
    a_31 = coef(f3, g1)
    a_32 = coef(f3, g2)
    
    print(f'{a_31},')
    print(f'{a_32},')
    
    def g3(x): 
        return f3(x) - a_31*g1(x) - a_32*g2(x)
    
    a_41 = coef(f4, g1)
    a_42 = coef(f4, g2)
    a_43 = coef(f4, g3)
    
    print(f'{a_41},')
    print(f'{a_42},')
    print(f'{a_43},')
   
    def g4(x): 
        return f4(x) - a_41*g1(x) - a_42*g2(x) - a_43*g3(x)
    
    
        
        