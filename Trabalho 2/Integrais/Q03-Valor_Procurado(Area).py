import math

def trapz(f, a, b, n):
    h = (b - a) / n
    soma = 0
    for k in range(1, n):
        soma += f(a + k * h)
    soma *= 2
    soma += f(a)
    soma += f(b)
    soma *= (h/2.0)
    print(f'{soma}',',')




def trapzPonto(x, y):
    tam = len(x) - 1
    somas = 0
    for i in range(tam):
        h = x[i+1] - x[i]
        somas += (h/2) * (y[i] + y[i+1])
    print(f'Area = {somas}')


x = [0.037, 0.039, 2.106, 3.54, 3.911, 4.386, 4.743]
y = [1.347, 1.353, 2.011, 2.696, 1.512, 1.443, 2.946]

'''''
def f(x):
    return math.sqrt(math.sin(math.cos(math.log(x**2+1)+2)+3)+4)

intervalo = [-1.562, 1.901]
subintervalos = [5, 11, 31, 60, 93, 103, 221, 446, 526, 835, 4922, 6223]


n = len(subintervalos)
for i in range(n):
    trapz(f, intervalo[0], intervalo[1], subintervalos[i])
'''''

trapzPonto(x, y)
