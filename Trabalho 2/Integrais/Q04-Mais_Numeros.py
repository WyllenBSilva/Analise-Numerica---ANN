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


x = [0.36, 0.644, 0.648, 1.089, 1.11, 1.471, 1.516, 1.733, 1.742, 1.912, 2.068, 2.234, 2.731, 2.928, 3.176, 3.437, 3.499, 3.777, 3.904, 4.118, 4.43, 4.604, 4.918]
y = [2.437, 2.964, 2.967, 2.738, 2.712, 2.276, 2.232, 2.071, 2.067, 2.008, 2.005, 2.055, 2.509, 2.759, 2.982, 2.88, 2.78, 1.984, 1.535, 1.026, 1.631, 2.477, 2.79]
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
