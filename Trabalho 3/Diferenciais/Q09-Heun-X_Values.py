

def heun(f,x0,y0,h,n,x_values):
    for k in range(1,n):
        m1 = f(x0,y0)
        m2 = f(x0 + h, y0 + h * m1)
        y0 += h * (m1+m2) / 2
        h = x_values[k] - x_values[k-1]
        x0 = x_values[k-1]
        yield[x0,y0]

    m1 = f(x0,y0)
    m2 = f(x0 + h, y0 + h * m1)
    y0 += h * (m1+m2) / 2
    h = x_values[n-1] - x_values[n-2]
    x0 = x_values[k-1]
    yield[x0,y0]

if __name__ == '__main__':
    #usar o wolpram alpha como resolvedor de equacoes diferencias.

    def f(x,y):
        func = y * (2 - x) + x + 1
        return func

    
    x0 = 0.22565
    y0 = 1.16281
    x_values = [0.23145, 0.30974, 0.33127, 0.40109, 0.44726, 0.49614, 0.55678, 0.59496, 0.64463, 0.69769, 0.76588, 0.78952, 0.83745, 0.90147, 0.94887, 1.01815, 1.05373, 1.11847, 1.14671, 1.18626]

    n = 20 # nmro de iteracoes

    h = x_values[0] - x0

    r3 = heun(f,x0,y0, h,n,x_values)
    x3,y3 = zip(*r3)

    valores = str(y3)[1:-1] 
    print(valores)

    #ele so vai pedir o valor das coordenadas y.
    

   

