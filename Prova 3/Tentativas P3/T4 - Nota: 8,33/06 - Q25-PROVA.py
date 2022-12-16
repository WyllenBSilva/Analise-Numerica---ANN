import math

p0 = 0.00178
birth_rate = 0.02657
death_rate = 0.00664
rebel_rate = 0.14937

def rk4(f, x0, y0,x_values, n):
    r = []
    h = x_values[0] - x0
    for _ in range(n):
        #realizar as iterações
        if (_>=1):
            h = x_values[_] - x_values[_-1]
        m1 = f(x0, y0)
        m2 = f(x0 + h/2, y0 + (h/2)*m1)
        m3 = f(x0 + h/2, y0 + (h/2)*m2)
        m4 = f(x0 + h, y0 + h *m3)
        yk = y0 + h * (m1+2*m2+2*m3+m4)/6
        #atualizando os valores
        x0 = x_values[_]
        y0 = yk
        #colocando valores na lista
        r.append((x0, y0))
    return r
    
# modificar valores de r e lambd    
def f(p, t):
    #rebel_rate = 0.16784
    #birth_rate = 0.01721
    k = rebel_rate * birth_rate
    return k * (1 - t)

# modificar valor de p0

''''
t0 = 0
p0 = 0.00179




'''
t0 = 0
#p0 = 0.00123


t_values = [0.0737, 0.80741, 1.91154, 2.54285, 2.9158, 3.80717, 4.3254, 5.10689, 5.71909, 6.4661, 6.85522, 7.92231, 8.17674, 9.19022, 9.46313, 10.56544, 10.8218, 11.43712, 12.37196, 12.77114, 13.65837, 14.30769, 15.26069, 15.44161, 16.48872, 16.93182, 17.87145, 18.53887, 19.08631, 19.6652, 20.45184, 21.01616, 21.61083, 22.27855, 22.90158, 23.64263, 24.59358, 25.01049, 25.73992, 26.59794, 27.24326, 27.83105, 28.37663, 28.99, 29.58034, 30.37428, 30.93115, 31.77515, 32.22373, 32.99525, 33.5571, 34.25935, 35.09929, 35.7471, 36.52419, 36.84644, 37.59372, 38.5573, 38.73385, 39.63599, 40.40943, 41.05748, 41.76297, 42.32552, 43.15945, 43.89829, 44.50783, 44.89378, 45.51979, 46.19347, 47.15089, 47.44481, 48.49976, 48.79945, 49.4638, 50.42192, 50.75968, 51.93244, 52.52928, 53.18816, 53.41304, 54.40992, 54.99838, 55.48247, 56.42092, 56.90447, 57.55497, 58.15823, 58.97267, 59.90823, 60.39528, 61.15916, 61.76393, 62.23396, 63.04473, 63.59239, 64.55918, 64.86569, 65.51439, 66.56173, 66.7682, 67.75013, 68.50475, 68.83134, 69.61336, 70.57481, 70.9061, 71.67726, 72.16352, 72.90366, 73.91431, 74.53885, 75.24226, 75.76677, 76.53077, 76.74449, 77.79043, 78.4201, 78.7919, 79.64961, 80.40504, 81.18725, 81.55597, 82.43301, 82.74565, 83.82023, 84.22361, 84.92398, 85.83384, 86.42408, 87.03194, 87.77024, 88.23995, 89.12047, 89.44766, 90.46288, 91.04895, 91.63818, 92.52829, 93.26655, 93.40678, 94.1373, 94.89206, 95.64669, 96.11386, 97.0782, 97.5743, 98.32488, 99.10564, 99.50561]

n = 150

r = rk4(f, t0, p0, t_values, n)

runge = []
for yi in r:
    runge.append(yi[1])


''''
t0 = 0





'''
# solução exata:
# modificar valores de r, lambd e coef 

''''Considerando p(t0)=p0, com t0=0, p0=0.00159, λ=0.01046, μ=0.006 e r=0.11114, use o método de Runge-Kutta de ordem 4 para encontrar aproximações para a solução p(t) nos instantes'''
def p(t):
    #rebel_rate = 0.16784
    #birth_rate = 0.01721
    k = rebel_rate * birth_rate
    # resolver:
    # solve p'(t) = k * (1 - p(t)), p(0) = p0
    # no wolfram, substituindo o valor de p0 dado na questao, então:
    #solve p'(t) = k * (1 - p(t)), p(0) = 0.00179
    #death_rate = 0.00507

    #result em wolpram alpha, apos fazer "solve p'(t) = k * (1 - p(t)), p(0) = 0.00159"
    return 1 - death_rate * math.exp(-k*t)
    
for i in range(n):
    print(f"{runge[i]}, {abs(0)},")



''''
obs: dp(t)dt=rλ(1−p(t)). <<-- isso é o que é dado no enunciado

onde r = rebel_rate

lambda = birth_rate

sendo assim, k = r * lambda
k = rebel_rate * birth_rate

assim, dp(t)dt=k * (1−p(t)), simplificando: 
p'(t) = k * ( - p(t)), p(0) = p0 
'''




''''
t0 = 0



'''