import numpy as np
import math


def trapz(f, a, b, n):
    h = abs(b-a) / n
    sum_fx = 0
    for i in range(1, n):
        sum_fx += f(a+i*h)
    return (f(a) + 2 * sum_fx + f(b)) * h/2

def coeffs(func ,funcs, a, b, subintervalos):

    n = len(funcs)
    A = np.zeros((n, n), dtype=float)
    B = np.zeros(n, dtype=float)
    for i in range(n):
        for j in range(i,n):
            def f_ji(x):
                return funcs[j](x) * funcs[i](x)
            # trapz, ou quadratura... depende o que pedir
            A[i][j] = trapz(f_ji, a, b, subintervalos)
            if i != j:
                A[j][i] = A[i][j]
        ffi = lambda x: func(x) * funcs[i](x)
        # trapz, ou quadratura... depende o que pedir
        B[i] = trapz(ffi, a, b, subintervalos)
    return np.linalg.solve(A,B)

def build_func(s, var: str='x'):
    scope = {}
    scope['math'] = math
    func = f'def f({var}): return {s}'
    exec(func, scope)
    return scope['f']

def comb(c, funcs):
    def g(x):
        return sum(ci * fi(x) for ci, fi in zip(c, funcs))
    return g

if __name__ == '__main__':

    # mudar aqui

    a = -0.9945
    b = 2.46399

    x1=-0.24738
    x2=0.50023
    x3=1.6402

    subintervalo_para_coeficientes = 256
    subintervalo_para_erro = 512

    def func(x):
        # mudar aqui
        func = 2 * math.sin(x) + math.cos(-x**2)
        return func

    

    funcs_str =  funcs = ['1', 'x', 'x**2', 'x**3', 'x**4', 'x**5']
    funcs = []
    for func_str in funcs_str:
        f = build_func(func_str)
        funcs.append(f)

    c = coeffs(func, funcs, a , b , subintervalo_para_coeficientes)
    for i in c:
        print(f"{i}, ")

   


    t = np.linspace(a, b, 200)
    ft = [func(ti) for ti in t]
   

    g = comb(c, funcs)
    print(f'{g(x1)},')
    print(f'{g(x2)},')
    print(f'{g(x3)},')
    gt = [g(ti) for ti in t]

    def funcerro(x):
        return (func(x) - g(x))**2

    erro = trapz(funcerro,a,b, subintervalo_para_erro)
    print(erro)