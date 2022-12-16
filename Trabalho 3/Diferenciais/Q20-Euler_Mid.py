
def true_euler(f, k, x0, y0, h, n):
    for i in range(n):
        y0 += h * f(x0, y0, k)
        x0 += h
        yield[x0,y0]
        #print(f'x_{i + 1}={x0} e y_{i+1}={y0}')

def euler(f, x0, y0, h, n):
    vals = []
    for k in range(n):
        x0 += h
        xk = x0 + k*h
        y0 += h * f(xk, y0)
        vals.append([xk,y0])
    return vals

def euler_mid(f, k, x0, y0, h, n):
    for _ in range(n):
        m1 = f(x0, y0,k)
        m2 = f(x0 + h / 2, y0 + (h / 2) * m1,k)
        y0 = y0 + h * m2
        x0 += h
        yield[x0,y0]

'''''
Assuma que a população de um país em t=0 seja de 1805041 indivíduos, que a taxa de natalidade seja constante igual a λ=0.04157 e que ν=42541 seja a taxa de imigração anual. Use o método do ponto médio de Euler para estimar o número de indivíduos nessa população após 1 ano. Use tamanho do passo h=0.0625.
'''''
if __name__ == '__main__':
    def f(x, y, k):
        # y = P
        return k*y + 42541 #valor de v
    # t == x

    x0, y0 = 0.0, 1805041  # x0 = t, y0 = individuos
    h = 0.0625
    k = 0.04157 #lambda
    n = int(1 / h)


    r1 = euler_mid(f, k,x0, y0, h, n)
    #print(r1)
    x1, y1 = zip(*r1)
    #valores = str(y1)[1:-1]
    print(y1[-1]) # Ultimo valor da lista
    #print(valores)

    #r2 = euler_mid(f, x0, y0, h, n)
    #x2, y2 = zip(*r2)
    #print(y2)

    #plot 
    
