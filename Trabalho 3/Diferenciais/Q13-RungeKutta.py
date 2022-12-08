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


if __name__ == "__main__":
    
    def f(x,y):
        func = y * (1 - x) + x + 2
        return func

    x0 = 0.83728
    y0 = 0.93994
    h = 0.125
    b = 0.81671

    n = 10

    r5 = RungeKutta2(f,x0,y0,h,n,b)
    x5,y5 = zip(*r5)

    valores = str(y5)[1:-1] 
    print(valores)


