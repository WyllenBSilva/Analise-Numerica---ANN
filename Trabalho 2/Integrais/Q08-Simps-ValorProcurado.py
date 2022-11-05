import math

def simps(f, a, b, n):
    if n % 2 != 0 or n < 1:
        raise ValueError("n deve ser par e maior q 1")
    h = (b - a) / n
    soma_odd, soma_even = 0, 0
    for k in range(1,n,2):
        soma_odd += f(a+k*h)
    for k in range(2,n,2):
        soma_even += f(a + k * h)
    return (h/3) * (f(a) + 4 * soma_odd + 2 * soma_even + f(b))


def simp(x0,x1,x3,y0,y1,y2):
    return ((x1-x0)/3)*(y0+4*y1+y2)

def simpsPonto(x, y):
    tam = (len(x) - 1) // 2
    somas = 0
    k = 0
    for i in range(tam):
        somas += simp(x[k],x[k+1],x[k+2],y[k],y[k+1],y[k+2])
        k += 2
    print(f'Valor Procurado:  {somas}')


#x = [1.566, 2.356, 3.146, 3.8185, 4.491]
#y = [2.187, 2.126, 2.967, 1.835, 1.922]

#x = [0.985, 2.1655, 3.346, 3.9375, 4.529]
#y = [2.857, 2.027, 2.971, 1.425, 2.112]

#x = [2.239, 2.272, 2.305, 3.119, 3.933]
#y = [2.057, 2.074, 2.093, 2.95, 1.44]

x = [1.507, 1.695, 1.883, 2.4545, 3.026]
y = [2.241, 2.093, 2.014, 2.205, 2.869]

simpsPonto(x, y)

'''''
def f(x):
    return math.sqrt(math.sin(math.cos(math.log(x**2+1)+2)+3)+4)

intervalo = [-1.995, 1.755]
subintervalos = [8, 16, 28, 68, 84, 110, 140, 170, 184, 226, 384]

n = len(subintervalos)
for i in range(n):
    print(simps(f, intervalo[0], intervalo[1], subintervalos[i]),',')
'''''



