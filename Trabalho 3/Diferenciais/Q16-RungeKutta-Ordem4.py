

def RK4(f,x0,y0,h,n):
    r = []
    for _ in range(n):

        m1 = f(x0,y0)
        #x0 =+ (h/2)
        m2 = f(x0+ h / 2, y0 + (h/2) * m1) 
        m3 = f(x0 + h / 2, y0 + (h/2) * m2)
        #x0 =+ (h/2)
        m4 = f(x0 + h, y0 + h * m3)
        yk = y0 + h * (m1 + 2 * m2 + 2 * m3 + m4) / 6
        #atualizar x0 e y0
        x0 += h
        y0 = yk
        r.append((x0,y0))
    return r




if __name__ == "__main__":

    


    def f(x,y):
        func = y * (1 - x) + x + 2 
        return func

    x0 = 0.7704
    y0 = 1.0838
    h = 0.125
    
    n = 10

    rk4 = RK4(f,x0,y0,h,n)
    #print(rk4)
    x4,y4 = zip(*rk4)

    valores = str(y4)[1:-1] 
    print(valores)
    
