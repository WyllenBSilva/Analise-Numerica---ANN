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


x = [0.032, 0.375, 0.39, 0.405, 0.419, 0.434, 0.44, 0.553, 0.755, 0.883, 1.092, 1.417, 1.635, 2.493, 2.959, 3.487, 3.821, 3.975, 4.093, 4.328, 4.852, 4.859, 4.994]
y = [1.332, 2.48, 2.522, 2.563, 2.599, 2.636, 2.65, 2.866, 3.0, 2.948, 2.734, 2.333, 2.133, 2.241, 2.795, 2.802, 1.826, 1.312, 1.055, 1.24, 2.961, 2.949, 2.445]
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
