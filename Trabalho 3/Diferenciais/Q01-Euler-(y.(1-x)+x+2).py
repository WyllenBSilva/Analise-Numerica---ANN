
def euler(f,x0,y0,h,n):
    for _ in range(n):
        y0 += h * f(x0,y0)
        x0 += h
        yield x0,y0
        #print(f'x_{k+1}={x0} e y_{k+1}={y0}')
    


if __name__ == '__main__':
    #usar o wolpram alpha como resolvedor de equacoes diferencias.

    import numpy as np

    def f(x,y):
        func = y * (1 - x) + x + 2
        return func
    
    x0 = 1.49761
    y0 = 2.97794
    h = 0.125

    n = 10 # nmro de iteracoes

    x,y = zip(*euler(f,x0,y0,h,n))
    #print(x)
    valores = str(y)[1:-1] 
    print(valores)

    #ele so vai pedir o valor das coordenadas y.
    

    #apenas para visualizacao
    '''''
    import matplotlib.pyplot as plt
    def sol(x):
        return -x + 4*np.exp(x-1)-1

    t = np.linspace(x0,(n+1)*h,200)
    sol_t = [sol(ti) for ti in t]

    plt.plot(t,sol_t,color='blue')
    plt.scatter(x,y,c='orange')
    plt.savefig('euler.png')
    '''''
    #print(euler(f,x0,y0,h,n))
    #gen = euler(f,x0,y0,h,n)
    #print(next(gen))
    ##print(next(gen))
    #print(list(gen)) # calcula todos de uma vez

