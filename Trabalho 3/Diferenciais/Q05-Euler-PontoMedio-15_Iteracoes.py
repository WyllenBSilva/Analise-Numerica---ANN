

def euler_mid(f, x0, y0, h, n):
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h / 2, y0 + (h / 2) * m1)
        y0 = y0 + h * m2
        x0 += h
        yield x0, y0

if __name__ == '__main__':
    def f(x, y):
        return y * (2 - x) + x + 1
    
    x0 = 1.05122
    y0 = 0.52131
    h = 0.12087

    n = 15


    r2 = euler_mid(f, x0, y0, h, n) #euler ponto medio
    x2, y2 = zip(*r2)

    valores = str(y2)[1:-1] 
    print(valores)

