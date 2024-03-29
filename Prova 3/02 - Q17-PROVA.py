import math
import numpy as np


def trapz(f, a, b, n):
    h = abs(b - a) / n
    sum_fx = 0

    for i in range(1, n):
        sum_fx += f(a + i * h)

    return (f(a) + 2 * sum_fx + f(b)) * h / 2

def simps(f, a, b, n):
    if n % 2 != 0:
        print('O valor n deve ser par')
        return None

    num_parabolas = n / 2
    soma = 0
    h = (b - a) / n

    for i in range(int(num_parabolas)):
        x0 = a + (2 * i) * h
        x1 = a + (2 * i + 1) * h
        x2 = a + (2 * i + 2) * h
        soma += f(x0) + 4 * f(x1) + f(x2)

    soma *= h / 3

    return soma


def coef(f,g): 


    a=-1.18648
    b=1.18711

    n = 256
    func = lambda x: (f(x) * g(x) ) 
    func2 = lambda x: g(x) * g(x)
    numer = simps(change(func,a,b),-1,1,n)
    denom = simps(change(func2,a,b),-1,1,n)
    
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
    def f5(x): return x**4
    def f6(x): return x**5
    def f7(x): return x**6
    def f8(x): return x**7
    def f9(x): return x**8
    def f10(x): return x**9

    
    def g1(x): return f1(x)

    a_21 =  coef(f2, g1)
    print(f'{a_21},')
    
    def g2(x): return f2(x) - a_21*g1(x)
    
    a_31 = coef(f3, g1)
    a_32 = coef(f3, g2)
    
    print(f'{a_31},')
    print(f'{a_32},')
    
    def g3(x): return f3(x) - a_31*g1(x) - a_32*g2(x)
    
    a_41 = coef(f4, g1)
    a_42 = coef(f4, g2)
    a_43 = coef(f4, g3)
    
    print(f'{a_41},')
    print(f'{a_42},')
    print(f'{a_43},')
   
    def g4(x): return f4(x) - a_41*g1(x) - a_42*g2(x) - a_43*g3(x)

    a_51 = coef(f5, g1)
    a_52 = coef(f5, g2)
    a_53 = coef(f5, g3)
    a_54 = coef(f5, g4)
    
    print(f'{a_51},')
    print(f'{a_52},')
    print(f'{a_53},')
    print(f'{a_54},')
   
    def g5(x): return f5(x) - a_51*g1(x) - a_52*g2(x) - a_53*g3(x) - a_54*g4(x)

    a_61 = coef(f6, g1)
    a_62 = coef(f6, g2)
    a_63 = coef(f6, g3)
    a_64 = coef(f6, g4)
    a_65 = coef(f6, g5)
    
    print(f'{a_61},')
    print(f'{a_62},')
    print(f'{a_63},')
    print(f'{a_64},')
    print(f'{a_65},')
   
    def g6(x): return f6(x) - a_61*g1(x) - a_62*g2(x) - a_63*g3(x) - a_64*g4(x) - a_65*g5(x)

    a_71 = coef(f7, g1)
    a_72 = coef(f7, g2)
    a_73 = coef(f7, g3)
    a_74 = coef(f7, g4)
    a_75 = coef(f7, g5)
    a_76 = coef(f7, g6)
    
    print(f'{a_71},')
    print(f'{a_72},')
    print(f'{a_73},')
    print(f'{a_74},')
    print(f'{a_75},')
    print(f'{a_76},')
   
    def g7(x): return f7(x) - a_71*g1(x) - a_72*g2(x) - a_73*g3(x) - a_74*g4(x) - a_75*g5(x) - a_76*g6(x)

    a_81 = coef(f8, g1)
    a_82 = coef(f8, g2)
    a_83 = coef(f8, g3)
    a_84 = coef(f8, g4)
    a_85 = coef(f8, g5)
    a_86 = coef(f8, g6)
    a_87 = coef(f8, g7)
    
    print(f'{a_81},')
    print(f'{a_82},')
    print(f'{a_83},')
    print(f'{a_84},')
    print(f'{a_85},')
    print(f'{a_86},')
    print(f'{a_87},')
   
    def g8(x): return f8(x) - a_81*g1(x) - a_82*g2(x) - a_83*g3(x) - a_84*g4(x) - a_85*g5(x) - a_86*g6(x) - a_87*g7(x)

    a_91 = coef(f9, g1)
    a_92 = coef(f9, g2)
    a_93 = coef(f9, g3)
    a_94 = coef(f9, g4)
    a_95 = coef(f9, g5)
    a_96 = coef(f9, g6)
    a_97 = coef(f9, g7)
    a_98 = coef(f9, g8)
    
    print(f'{a_91},')
    print(f'{a_92},')
    print(f'{a_93},')
    print(f'{a_94},')
    print(f'{a_95},')
    print(f'{a_96},')
    print(f'{a_97},')
    print(f'{a_98},')
   
    def g9(x): return f9(x) - a_91*g1(x) - a_92*g2(x) - a_93*g3(x) - a_94*g4(x) - a_95*g5(x) - a_96*g6(x) - a_97*g7(x) - a_98*g8(x)

    a_11 = coef(f10, g1)
    a_12 = coef(f10, g2)
    a_13 = coef(f10, g3)
    a_14 = coef(f10, g4)
    a_15 = coef(f10, g5)
    a_16 = coef(f10, g6)
    a_17 = coef(f10, g7)
    a_18 = coef(f10, g8)
    a_19 = coef(f10, g9)
    
    print(f'{a_11},')
    print(f'{a_12},')
    print(f'{a_13},')
    print(f'{a_14},')
    print(f'{a_15},')
    print(f'{a_16},')
    print(f'{a_17},')
    print(f'{a_18},')
    print(f'{a_19},')
   
    def g10(x): return f10(x) - a_11*g1(x) - a_12*g2(x) - a_13*g3(x) - a_14*g4(x) - a_15*g5(x) - a_16*g6(x) - a_17*g7(x) - a_18*g8(x) - a_19*g9(x) 



    
    
        
        