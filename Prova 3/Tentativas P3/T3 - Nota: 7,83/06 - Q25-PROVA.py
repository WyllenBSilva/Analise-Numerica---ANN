import math

p0 = 0.00119
birth_rate = 0.02759
death_rate = 0.00931
rebel_rate = 0.18944

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

t_values = [0.24551, 0.93636, 1.70698, 2.18187, 3.08549, 3.42404, 4.28081, 4.75785, 5.68369, 6.5761, 7.26137, 7.66362, 8.4476, 9.01463, 9.54979, 10.33914, 11.25907, 11.63018, 12.22274, 13.2518, 13.65174, 14.58419, 14.96377, 15.85929, 16.10541, 16.76297, 17.52595, 18.07296, 19.03445, 19.68953, 20.42197, 20.80258, 21.69693, 22.48599, 23.01648, 23.58858, 24.45883, 24.94322, 25.459, 26.53425, 27.12641, 27.92801, 28.23077, 28.74814, 29.82219, 30.38328, 31.03414, 31.93306, 32.40811, 32.9888, 33.58158, 34.28527, 35.17728, 35.53451, 36.51427, 36.74759, 37.72886, 38.25725, 38.91795, 39.66473, 40.33929, 41.2013, 41.6702, 42.55836, 42.74239, 43.47711, 44.57791, 45.11119, 45.87382, 46.35542, 47.04292, 47.45243, 48.47064, 49.03299, 49.6557, 50.20709, 50.83317, 51.55988, 52.22441, 52.74793, 53.41593, 54.33793, 55.05314, 55.9027, 56.4646, 57.13897, 57.46811, 58.5354, 59.25544, 59.81409, 60.28201, 60.93404, 61.898, 62.29347, 63.12625, 63.69486, 64.46855, 64.93056, 65.67271, 66.23741, 66.89391, 67.55744, 68.09446, 68.98644, 69.59466, 70.1127, 71.24232, 71.79253, 72.34377, 73.21368, 73.68022, 74.14042, 75.01837, 75.52658, 76.1573, 76.8566, 77.42311, 78.21382, 78.8382, 79.77283, 80.55795, 80.84533, 81.72101, 82.18878, 82.91167, 83.65701, 84.10126, 84.97614, 85.73735, 86.49248, 86.81542, 87.7052, 88.186, 89.22666, 89.67083, 90.27941, 91.26311, 91.83379, 92.25264, 93.14667, 93.52433, 94.36855, 94.9317, 95.49601, 96.10756, 96.91404, 97.44118, 98.08448, 98.96772, 99.44099]

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