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


x = [0.14, 0.7295, 1.319, 1.3605, 1.402, 1.6095, 1.817, 1.855, 1.893, 2.0495, 2.206, 2.213, 2.22, 2.408, 2.596, 2.7845, 2.973, 3.686, 4.399, 4.6705, 4.942]
y = [1.687, 2.999, 2.447, 2.398, 2.35, 2.152, 2.033, 2.021, 2.011, 2.002, 2.042, 2.045, 2.048, 2.166, 2.348, 2.577, 2.812, 2.295, 1.496, 2.75, 2.696]


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



