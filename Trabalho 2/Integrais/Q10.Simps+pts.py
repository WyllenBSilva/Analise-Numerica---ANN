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


x = [0.128, 0.2375, 0.347, 0.461, 0.575, 0.8005, 1.026, 1.0425, 1.059, 1.3985, 1.738, 1.8005, 1.863, 1.8645, 1.866, 2.0305, 2.195, 2.2335, 2.272, 2.452, 2.632, 2.713, 2.794, 2.863, 2.932, 2.964, 2.996, 3.0205, 3.045, 3.1205, 3.196, 3.546, 3.896, 3.918, 3.94, 3.9835, 4.027, 4.279, 4.531, 4.5725, 4.614, 4.6285, 4.643, 4.7505, 4.858]
y = [1.645, 2.035, 2.398, 2.698, 2.896, 2.991, 2.813, 2.794, 2.774, 2.354, 2.069, 2.04, 2.019, 2.018, 2.018, 2.001, 2.038, 2.054, 2.074, 2.203, 2.389, 2.487, 2.589, 2.678, 2.763, 2.801, 2.837, 2.863, 2.888, 2.951, 2.99, 2.683, 1.562, 1.488, 1.417, 1.288, 1.177, 1.114, 2.122, 2.328, 2.523, 2.586, 2.646, 2.959, 2.951]


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



