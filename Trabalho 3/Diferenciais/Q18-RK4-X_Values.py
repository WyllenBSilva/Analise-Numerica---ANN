
def RK4(f,x0,y0,h,n,x_values):
    r = []
    for k in range(1,n):
        m1 = f(x0,y0)
        m2 = f(x0+ h / 2, y0 + (h/2) * m1) 
        m3 = f(x0 + h / 2, y0 + (h/2) * m2)
        m4 = f(x0 + h, y0 + h * m3)
        yk = y0 + h * (m1 + 2 * m2 + 2 * m3 + m4) / 6
        h = x_values[k] - x_values[k-1]
        x0 = x_values[k-1]
        y0 = yk
        yield[x0,y0]

    m1 = f(x0,y0)
    m2 = f(x0+ h / 2, y0 + (h/2) * m1) 
    m3 = f(x0 + h / 2, y0 + (h/2) * m2)
    m4 = f(x0 + h, y0 + h * m3)
    yk = y0 + h * (m1 + 2 * m2 + 2 * m3 + m4) / 6
    h = x_values[n-1] - x_values[n-2]
    x0 = x_values[k-1]
    y0 = yk
    yield[x0,y0]

if __name__ == "__main__":

    def f(x,y):
        func = y * (1 - x) + x + 2
        return func
    

    x0 = 1.2057
    y0 = 1.3079
    x_values = [1.2402, 1.2918, 1.3165, 1.3678, 1.4416, 1.4724, 1.544, 1.597, 1.6264, 1.6745, 1.7187, 1.7677, 1.8169, 1.8615, 1.9284, 1.9746, 2.0462, 2.0761, 2.1393, 2.1785]

    n = 20

    h = x_values[0] - x0
    rk4 = RK4(f,x0,y0,h,n,x_values)
    #print(rk4)
    x4,y4 = zip(*rk4)

    valores = str(y4)[1:-1] 
    print(valores)
    
