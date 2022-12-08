def ralston(f,x0,y0,h,n):
    for k in range(n):
        m1 = f(x0,y0)
        m2 = f(x0+ 0.75 * h, y0+ 0.75 * h * m1)
        y0 += h * (m1+ 2 * m2) / 3
        x0 += h
        yield [x0,y0]


if __name__ == "__main__":

    def f(x,y):
        func = y * (2 - x) + x + 1
        return func

    x0 = 1.52029
    y0 = 1.97107
    h = 0.15727

    n= 15
    
    r4 = ralston(f,x0,y0,h,n)
    x4,y4 = zip(*r4)

    valores = str(y4)[1:-1] 
    print(valores)
