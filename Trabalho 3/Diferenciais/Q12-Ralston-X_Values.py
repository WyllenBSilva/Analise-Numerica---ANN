def ralston(f,x0,y0,h,n,x_values):
    for k in range(1,n):
        m1 = f(x0,y0)
        m2 = f(x0+ 0.75 * h, y0+ 0.75 * h * m1)
        y0 += h * (m1+ 2 * m2) / 3
        h = x_values[k] - x_values[k-1]
        x0 = x_values[k-1]
        yield [x0,y0]
    
    m1 = f(x0,y0)
    m2 = f(x0+ 0.75 * h, y0+ 0.75 * h * m1)
    y0 += h * (m1+ 2 * m2) / 3
    h = x_values[n-1] - x_values[n-2]
    x0 = x_values[k-1]
    yield [x0,y0]




if __name__ == "__main__":

    def f(x,y):
        func = y * (2 - x) + x + 1
        return func

    x0 = 1.12204
    y0 = 1.20136
    x_values = [1.14287, 1.1938, 1.26073, 1.27919, 1.35245, 1.4047, 1.45396, 1.49589, 1.56627, 1.60953, 1.65671, 1.71468, 1.74428, 1.77942, 1.83464, 1.87853, 1.96206, 1.98071, 2.02773, 2.11572]

    n= 20
    
    h = x_values[0] - x0
    r4 = ralston(f,x0,y0,h,n,x_values)
    x4,y4 = zip(*r4)

    valores = str(y4)[1:-1] 
    print(valores)
