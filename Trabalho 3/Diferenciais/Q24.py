"""Em um circuito com tensão aplicada E e com resistência R, indutância 
L e capacitância C em paralelo, a corrente i satisfaz a equação diferencial
didt=Cd2Edt2+1RdEdt+1LE.
Suponha que C=0.2311farads, R=1.3534ohm, L=1.5026henrie e que a tensão seja dada por
E(t)=e−0.0549πtsin(2t−π).
Se i(t0)=i0, com t0=0 e i0=0, use o método de Heun para encontrar estimativas
para a corrente i nos pontos
t1=0.0853, t2=0.124, t3=0.2613, t4=0.3842, t5=0.4704, t6=0.5809, t7=0.6249, 
t8=0.7385, t9=0.8313, t10=0.9542, ...... t149=14.8388 e t150=14.939."""

import numpy as np



def euler(f, x0, y0, h, n):
    vals = []
    for k in range(n):
        y0 += h*f(x0, y0)
        x0 += h
        vals.append([x0, y0])
    return vals


# b = 1
def euler_mid(f, x0, y0, h, n):
    vals = []
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h / 2, y0 + (h/2) * m1)
        y0 += h*m2
        x0 += h
        vals.append([x0, y0])
    return vals


# b = 1/2
def heun(f, x0, y0, h, n):
    vals = []
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h, y0 + h*m1)
        y0 += h*(m1+m2)/2
        x0 += h
        vals.append([x0, y0])
    return vals


# b = 2/3
# def ralston(f, x0, y0, h, n):
#     vals = []
#     for _ in range(n):
#         m1 = f(x0, y0)
#         m2 = f(x0 + 0.75*h, y0 + 0.75*h*m1)
#         y0 = h*(m1 + 2*m2)/3
#         x0 += h
#         vals.append([x0, y0])
#     return vals


# padrao = euler_mid
def rk2(f, x0, y0, h, n, b=1.0):
    # b = 1 => metodo = euler_mid
    # b = 1/2 => metodo = heun
    # b = 2/3 => metodo = ralston
    vals = []
    a = 1-b
    p = 1/(2*b)
    q = p
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + p*h, y0 + q*h*m1)
        y0 += (a*m1 + b*m2)*h
        x0 += h
        vals.append([x0, y0])
    return vals


def rk2_h_variavel(f, x0, y0, n, b, x_values):
    # b = 1 => metodo = euler_mid
    # b = 1/2 => metodo = heun
    # b = 2/3 => metodo = ralston
    vals = []
    a = 1-b
    p = 1/(2*b)
    q = p
    for i in range(n):
        if i == 0:
            h = x_values[0] - x0
        else:
            h = x_values[i] - x_values[i-1]
        m1 = f(x0, y0)
        m2 = f(x0 + p*h, y0 + q*h*m1)
        y0 += (a*m1 + b*m2)*h
        x0 += h
        vals.append([x0, y0])
    return vals


def diff(a, b):
    return sum((ai - bi)**2 for ai, bi in zip(a, b))


def f(x, y):
    return y * (1 - x) + x + 2


def g(t, i):

    ''''Suponha que C=0.2872farads, R=1.0588ohm, L=1.8899henrie e que a tensão seja dada por
    E(t)=e−0.0714πtsin(2t−π).
    '''
    c = 0.2872
    r = 1.0588
    l = 1.8899

    # considerando a função e(t) = e^(-e_value*pi*t)*sin(2*t-pi)
    # se e^(-0.0549*pi*t) => e_value = 0.0549
    e_value = 0.0714

    def e(t):
        return np.exp(-e_value*np.pi*t)*np.sin(2*t-np.pi)

    def e_(t):
        return np.exp(-e_value*np.pi*t)*(2*np.cos(np.pi-2*t)+e_value*np.pi*np.sin(np.pi-2*t))

    def e__(t):
        return np.exp(-e_value*np.pi*t)*((4-pow(e_value, 2)*pow(np.pi, 2))*np.sin(np.pi-2*t)-4*e_value*np.pi*np.cos(np.pi-2*t))

    return c*e__(t) + (1/r)*e_(t) + (1/l)*e(t)


if __name__ == '__main__':

    x0, y0 = 0,0
    h = 0.101
    n = 150
    b = 1/2
    t_values = [0.0556, 0.1575, 0.2824, 0.3363, 0.4284, 0.5699, 0.6547, 0.7847, 0.8302, 0.9158, 1.0647, 1.1577, 1.2686, 1.3835, 1.4156, 1.5837, 1.688, 1.7149, 1.8654, 1.9602, 2.0572, 2.1528, 2.2826, 2.3155, 2.4374, 2.5736, 2.6731, 2.7357, 2.8231, 2.9853, 3.0226, 3.1516, 3.2315, 3.3789, 3.4686, 3.5846, 3.6817, 3.7646, 3.8896, 3.9447, 4.0769, 4.1697, 4.2841, 4.3532, 4.4509, 4.5353, 4.6273, 4.7154, 4.8667, 4.9416, 5.0738, 5.1104, 5.2633, 5.3107, 5.4794, 5.5645, 5.6841, 5.7654, 5.813, 5.929, 6.0629, 6.1695, 6.2438, 6.3103, 6.4804, 6.5806, 6.6268, 6.7307, 6.8141, 6.9623, 7.0471, 7.1404, 7.2117, 7.3524, 7.4444, 7.5412, 7.6419, 7.7183, 7.8743, 7.9697, 8.0718, 8.1112, 8.2269, 8.3311, 8.423, 8.5693, 8.6773, 8.7515, 8.8136, 8.9762, 9.0874, 9.1816, 9.2841, 9.375, 9.4842, 9.5806, 9.6384, 9.725, 9.8185, 9.9343, 10.0875, 10.1236, 10.2395, 10.3628, 10.4139, 10.5263, 10.6685, 10.724, 10.8574, 10.9841, 11.0359, 11.1845, 11.2431, 11.3604, 11.474, 11.5514, 11.6557, 11.7111, 11.8118, 11.9101, 12.0111, 12.1507, 12.2145, 12.3657, 12.4449, 12.552, 12.6611, 12.7469, 12.8346, 12.9295, 13.0337, 13.1897, 13.2111, 13.3408, 13.4234, 13.5785, 13.6541, 13.7738, 13.8853, 13.9125, 14.0816, 14.1421, 14.2549, 14.3471, 14.4453, 14.5624, 14.6481, 14.724, 14.8586, 14.9652]
    """observar o valor de b na função para qual médoto é usado:
    --> b = 1 => metodo = euler_mid
    --> b = 1/2 => metodo = heun
    --> b = 2/3 => metodo = ralston"""
    
    
    # metodo1 = euler(f, x0, y0, h, n)
    # metodo2 = euler_mid(f, x0, y0, h, n)
    # metodo3 = heun(f, x0, y0, h, n)
    # metodo4 = ralston(f, x0, y0, h, n)
    # metodo5 = rk2(g, x0, y0, h, n, b)
    metodo6 = rk2_h_variavel(g, x0, y0, n, b, t_values)

    indice = [i for i in range(n)]
    lista_x, lista_y = zip(*metodo6)

    for i, xi, yi in zip(indice, lista_x, lista_y):
        # print(f'x{i} = {xi} => y{i} = {yi}')
        print(f'{yi},', end='')