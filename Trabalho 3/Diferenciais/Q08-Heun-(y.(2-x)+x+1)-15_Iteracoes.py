def heun(f,x0,y0,h,n):
    for _ in range(n):
        m1 = f(x0,y0)
        m2 = f(x0 + h, y0 + h * m1)
        y0 += h * (m1+m2) / 2
        x0 += h
        yield[x0,y0]
    
    

if __name__ == '__main__':

    def f(x,y):
        func = y * (2 - x) + x + 1
        return func

    
    
    x0 = 1.84893
    y0 = 0.57835
    h = 0.17016

    n = 15
    
    r3 = heun(f,x0,y0, h,n)
    x3,y3 = zip(*r3)

    valores = str(y3)[1:-1] 
    print(valores)





