import math
import numpy as np

def trapz(f, a, b, n):
    h = abs(b - a) / n
    sum_fx = 0

    for i in range(1, n):
        sum_fx += f(a + i * h)

    return (f(a) + 2 * sum_fx + f(b)) * h / 2


def trapz_romberg(f, a, b, h):
    n = int((b - a) / h)
    soma = 0

    for k in range(1, n):
        soma += f(a + k * h)

    return (h / 2) * (f(a) + 2 * soma + f(b))


def romberg(coluna_f1):
    coluna_f1 = [i for i in coluna_f1]
    n = len(coluna_f1)
    for j in range(n - 1):
        temp_col = [0] * (n - 1 - j)
        for i in range(n - 1 - j):
            power = j + 1
            temp_col[i] = (4 ** power * coluna_f1[i + 1] - coluna_f1[i]) / (4 ** power - 1)
        coluna_f1[:n - 1 - j] = temp_col
        # print(f'F_{j+2} = {temp_col}')
    return coluna_f1[0]


#Dá erro, mas roda mesmo assim.
def best_func(f, funcs, a, b, method: ['trapz', 256]):
    k = len(funcs)

    A = [[0 for _ in range(k)] for _ in range(k)]
    B = []

    for i in range(k):
        for j in range(k):
            if j >= i:
                def f_ij(x):
                    return funcs[j](x) * funcs[i](x)

                if method[0] == 'trapz':
                    A[i][j] = trapz(f_ij, a, b, method[1])
                elif method[0] == 'romberg':
                    tam = int(method[1] / 2)
                    hs = [method[2] / 2 ** ki for ki in range(tam)]
                    coluna_f1 = [trapz_romberg(f_ij, a, b, hi) for hi in hs]
                    A[i][j] = romberg(coluna_f1)

            else:
                A[i][j] = A[j][i]

        def ffi(x):
            return f(x) * funcs[i](x)

        if method[0] == 'trapz':
            B.append(trapz(ffi, a, b, method[1]))
        elif method[0] == 'romberg':
            tam = int(method[1] / 2)
            hs = [method[2] / 2 ** ki for ki in range(tam)]
            coluna_f1 = [trapz_romberg(ffi, a, b, hi) for hi in hs]
            B.append(romberg(coluna_f1))

    A = np.array(A, dtype=float)
    B = np.array(B, dtype=float)

    return np.linalg.solve(A, B)


def criar_funcoes(lista_funcoes):
    for indice, funcao in enumerate(lista_funcoes):
        scope = {
            'lista_funcoes': lista_funcoes,
            'indice': indice,
            'funcao': funcao,
            'math': math
        }

        exec('lista_funcoes[indice] = lambda x:eval(funcao)', scope)

    return lista_funcoes


def simps(f, a, b, n):
    if n % 2 != 0 or n < 1:
        raise ValueError("n deve ser par e maior q 1")
    h = (b - a) / n
    soma_odd, soma_even = 0, 0
    for k in range(1,n,2):
        soma_odd += f(a+k*h)
    for k in range(2,n,2):
        soma_even += f(a + k * h)
    return (h/3) * (f(a) + 4 * soma_odd + 2 * soma_even + f(b))

def simp(x0,x1,x3,y0,y1,y2):
    return ((x1-x0)/3)*(y0+4*y1+y2)

def simpsPonto(x, y):
    tam = (len(x) - 1) // 2
    somas = 0
    k = 0
    for i in range(tam):
        somas += simp(x[k],x[k+1],x[k+2],y[k],y[k+1],y[k+2])
        k += 2
    print(f'{somas}')



def f(x):
    return x**2 * math.cos(x * math.sin(math.log(1 + x**2)))


if __name__ == '__main__':
    
    
    
    

    funcs = ['2', 'x - 1', 'x**2 + 1', 'x**3 + x - 3', '0.5 * x**4 - 3 * x**2 + 1', 'x**5 - 4 * x + 2', 'x**7-x']
    a = -2.19602    
    b = 2.16094

    x1=-0.95603
    x2=-0.32731
    x3=0.88641

    values = [x1,x2,x3]
    order = 8
    h = (b - (a)) / 10
    method = ['romberg', order, h]



    funcs = criar_funcoes(funcs)

    coefs = best_func(f, funcs, a, b, method)

    coefs = [ci for ci in coefs]

    for i in coefs:
        print(f'{i}, ')


    def g(x):
        return sum(ci * fi(x) for ci, fi in zip(coefs, funcs))


    for x in values:
        print(f'{g(x)}, ')



    def func_erro(x):
        return (f(x) - g(x)) ** 2



    erro = simps(func_erro, a, b, 256)

    print(f'{erro}')

