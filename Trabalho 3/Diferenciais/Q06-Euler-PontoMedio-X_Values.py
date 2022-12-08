
def euler(f,x0,y0,h,n,x_values):
    for k in range(1,n):
        
        m1 = f(x0, y0)
        m2 = f(x0 + h / 2, y0 + (h / 2) * m1)
        y0 += h * m2
        h = x_values[k] - x_values[k-1]
        x0 = x_values[k-1]
        yield x0,y0
        #print(f'x_{k+1}={x0} e y_{k+1}={y0}')
    
    m1 = f(x0, y0)
    m2 = f(x0 + h / 2, y0 + (h / 2) * m1)
    h = x_values[n-1] - x_values[n-2]
    x0 = x_values[k-1]
    y0 += h * m2
    yield x0,y0




if __name__ == '__main__':
    #usar o wolpram alpha como resolvedor de equacoes diferencias.

    import numpy as np

    def f(x,y):
        func = y * (2 - x) + x + 1
        return func

    
    x0 = 0.6776
    y0 = 0.79123
    x_values = [0.69647, 0.74278, 0.79167, 0.85248, 0.91353, 0.93855, 1.02256, 1.05307, 1.11428, 1.14683, 1.19007, 1.24428, 1.31794, 1.34187, 1.38935, 1.46307, 1.48909, 1.55995, 1.60744, 1.63951]

    n = 20 # nmro de iteracoes

    h = x_values[0] - x0
    x,y = zip(*euler(f,x0,y0,h,n,x_values))
    #print(x)
    valores = str(y)[1:-1] 
    print(valores)

    #ele so vai pedir o valor das coordenadas y.
    

   

