def RungeKutta2(f,x0,y0,h,n,x_values,b:int=1):
    
    '''''
    B = 1 corresponde ao metodo do ponto medio de Euler.
    B = 1/2 corresponde ao metodo de Heun
    B = 2/3 corresponde ao metodo de Ralston

    Porém, não testei.
    '''''

    a = 1 - b
    p = 1 / ( 2 * b)
    q = p
    for k in range(1,n):
        m1 = f(x0,y0)
        m2 = f(x0 + p * h,y0 + q * h * m1)
        y0 = y0 + (a * m1 + b * m2) * h
        h = x_values[k] - x_values[k-1]
        x0 = x_values[k-1]
        yield[x0,y0]

    m1 = f(x0,y0)
    m2 = f(x0 + p * h,y0 + q * h * m1)
    y0 = y0 + (a * m1 + b * m2) * h
    h = x_values[n-1] - x_values[n-2]
    x0 = x_values[k-1]
    yield[x0,y0]




if __name__ == "__main__":
    
    def f(x,y):
        func = y * (1 - x) + x + 2
        return func

    x0 = 1.02684
    y0 = 0.42318
    x_values = [1.04389, 1.10879, 1.13574, 1.18679, 1.26222, 1.32169, 1.3355, 1.39575, 1.45922, 1.51653, 1.54229, 1.61164, 1.66655, 1.69245, 1.73215, 1.81815, 1.86788, 1.9194, 1.93781, 2.01558]
    b = 0.62567

    n = 20

    h = x_values[0] - x0
    r5 = RungeKutta2(f,x0,y0,h,n,x_values,b)
    x5,y5 = zip(*r5)

    valores = str(y5)[1:-1] 
    print(valores)


