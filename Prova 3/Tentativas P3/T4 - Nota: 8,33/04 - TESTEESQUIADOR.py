import math

#nao mudar valor de B.
def RK2(f, x0, y0, h, n, b=0.981):
    a = 1 - b
    p = 1 / (2 * b)
    q = p
    for _ in range(n):
        m1 = f(x0,y0)
        m2 = f(x0+p*h, y0+q*h*m1)
        y0 += (a * m1 + b * m2) * h
        x0 += h
        yield [x0,y0]


#Q11 Prova:
def f(x,y):
    return -y/(math.sqrt(9.42112**2 - y**2)) # a


#Se P0=(x0,y0), com x0=1.70097 e y0=4.16717, denota a posição inicial do esquiador. Use o método de Euler para estimar a posição do esquiador nos pontos xk=x0+kh, onde k=1,2,…,100. Suponha que a=9.42112 e use h=0.14927.

x0 = 1.70097
y0 = 4.16717
h = 0.14927


e = RK2(f,x0,y0, h,n=100)
for xi, yi in e:
    print(yi,',')