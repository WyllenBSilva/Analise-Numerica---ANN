def heun(f,x0,y0,h,n,k):
    for _ in range(n):
        m1 = f(x0,y0,k)
        m2 = f(x0 + h, y0 + h * m1,k)
        y0 += h * (m1+m2) / 2
        x0 += h
        yield[x0,y0]
    

''''
Assuma que a população de um país em t=0 seja de 1209307 indivíduos, que a taxa de natalidade seja constante igual a λ=0.03141 e que ν=44479 seja a taxa de emigração anual. Use o método de Heun para estimar o número de indivíduos nessa população após 1 ano. Use tamanho do passo h=0.0625.
 
 '''

if __name__ == '__main__':

    def f(x,y,k):
        return k*y - 44479 #valor de v

    
    
    x0 = 0 # t 
    y0 = 1209307 #individuos
    k = 0.03141  #lambda
    h = 0.0625

    n = int(1/h)
    
    r3 = heun(f,x0,y0, h,n,k)
    x3,y3 = zip(*r3)
    print(y3[-1])
    #valores = str(y3)[1:-1] 
    #print(valores)





