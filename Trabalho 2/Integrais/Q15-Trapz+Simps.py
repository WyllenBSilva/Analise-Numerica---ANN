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
    return somas



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
    return somas



#Use excel para copiar e colar as colunas e fazer com mais rapidez.
x = [0.0	,
0.75	,
1.5	,
2.25	,
3.0	,
3.75	,
4.5	,
5.25	,
6.0	,
6.75	,
7.5	,
8.25	,
9.0	,
9.75	,
10.5	,
11.25	,
12.0	,
]



y = [9.89	,
9.52	,
9.0	,
8.56	,
8.24	,
7.81	,
7.2	,
6.96	,
6.34	,
6.09	,
5.66	,
5.36	,
4.76	,
4.28	,
4.12	,
3.64	,
3.29	,

]





print("1 - Trapezio:  2 - Simpsons, ")
print(trapzPonto(x, y),',')
print(simpsPonto(x, y),',')


