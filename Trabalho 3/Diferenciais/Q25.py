import math

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
    rebel_rate = 0.11114
    birth_rate = 0.01046
    k = rebel_rate * birth_rate
    return k * (1 - t)

# modificar valor de p0    
t0 = 0
p0 = 0.00159
t_values = [0.10315, 0.88929, 1.64445, 2.099, 3.17351, 3.85009, 4.37943, 4.76354, 5.44615, 6.48899, 6.88179, 7.54978, 8.44672, 9.13905, 9.68464, 10.11619, 10.92662, 11.55769, 12.18138, 13.05819, 13.48543, 14.19743, 15.16537, 15.51242, 16.5026, 16.85559, 17.55593, 18.42355, 18.91382, 19.52208, 20.58496, 21.09447, 21.53568, 22.47801, 23.17866, 23.58937, 24.5564, 24.90074, 25.41982, 26.17875, 26.90668, 27.92487, 28.11961, 28.75182, 29.74732, 30.4723, 30.77558, 31.41657, 32.34671, 32.76678, 33.71867, 34.48939, 34.83309, 35.44131, 36.41283, 36.95873, 37.55998, 38.35131, 39.07797, 39.90824, 40.33749, 41.04228, 41.61837, 42.09783, 42.92567, 43.84235, 44.59039, 45.09267, 45.4533, 46.40387, 47.06867, 47.82134, 48.09191, 48.84579, 49.88392, 50.08706, 51.16906, 51.6724, 52.2772, 52.98736, 53.73478, 54.19281, 55.13999, 55.9217, 56.20907, 56.94611, 57.63577, 58.54186, 58.90123, 59.59673, 60.50842, 60.83597, 61.79275, 62.28792, 62.80848, 63.89824, 64.27849, 65.20637, 65.57558, 66.53898, 67.11812, 67.44528, 68.32648, 68.81262, 69.53422, 70.5189, 70.74535, 71.88872, 72.47961, 73.20039, 73.53626, 74.15991, 74.74701, 75.56402, 76.5407, 77.23448, 77.81309, 78.50123, 78.96173, 79.53106, 80.39136, 80.77405, 81.41503, 82.13563, 82.73479, 83.90525, 84.39463, 85.03902, 85.75604, 86.58696, 86.92591, 87.89067, 88.32327, 89.14511, 89.66786, 90.27043, 91.22801, 91.63778, 92.51001, 93.13986, 93.65532, 94.1249, 94.83577, 95.44184, 96.13502, 96.87681, 97.42387, 98.14118, 98.88445, 99.91049]
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
    rebel_rate = 0.11114
    birth_rate = 0.01046
    k = rebel_rate * birth_rate
    # resolver:
    # solve p'(t) = k * (1 - p(t)), p(0) = p0
    # no wolfram, substituindo o valor de p0 dado na questao, então:
    #solve p'(t) = k * (1 - p(t)), p(0) = 0.00159
    death_rate = 0.006

    #result em wolpram alpha, apos fazer "solve p'(t) = k * (1 - p(t)), p(0) = 0.00159"
    return 1 - death_rate * math.exp(-k*t)
    
for i in range(150):
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