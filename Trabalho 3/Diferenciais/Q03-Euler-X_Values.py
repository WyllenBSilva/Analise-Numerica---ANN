
def euler(f,x0,y0,h,n,x_values):
    for k in range(1,n):
        y0 += h * f(x0,y0)
        h = x_values[k] - x_values[k-1]
        x0 = x_values[k-1]
        yield x0,y0
        #print(f'x_{k+1}={x0} e y_{k+1}={y0}')
    
    h = x_values[n-1] - x_values[n-2]
    x0 = x_values[k-1]
    y0 += h * f(x0,y0)
    yield x0,y0
    


if __name__ == '__main__':
    #usar o wolpram alpha como resolvedor de equacoes diferencias.

    import numpy as np

    def f(x,y):
        func = y * (1 - x) + x + 2
        return func

    x0 = 0.31774
    y0 = 1.41849
    x_values = [0.3465, 0.39825, 0.44745, 0.48162, 0.54733, 0.60621, 0.62359, 0.68393, 0.73055, 0.77451, 0.85169, 0.87295, 0.95866, 0.99079, 1.04279, 1.0879, 1.14955, 1.18267, 1.2442, 1.30675]

    n = 20 # nmro de iteracoes

    h = x_values[0] - x0
    x,y = zip(*euler(f,x0,y0,h,n,x_values))
    #print(x)
    valores = str(y)[1:-1] 
    print(valores)

    #ele so vai pedir o valor das coordenadas y.
    

   

