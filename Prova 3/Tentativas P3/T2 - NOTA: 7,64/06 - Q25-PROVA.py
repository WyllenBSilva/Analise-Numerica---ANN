import math

p0 = 0.00123
birth_rate = 0.02158
death_rate = 0.00997
rebel_rate = 0.15915

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

t_values = [0.50622, 1.2087, 1.85291, 2.53676, 2.99479, 3.89652, 4.26943, 5.12815, 5.63051, 6.57582, 7.10933, 7.65166, 8.56374, 9.15842, 9.4502, 10.33131, 11.23847, 11.74071, 12.42104, 12.82965, 13.80689, 14.5728, 15.05218, 15.69688, 16.43412, 16.8648, 17.85926, 18.35624, 19.10416, 19.57042, 20.54816, 20.81281, 21.51504, 22.19977, 22.84291, 23.90881, 24.16717, 25.13815, 25.58517, 26.59051, 26.74494, 27.76223, 28.51436, 28.83456, 29.60609, 30.41969, 30.84661, 31.86282, 32.08014, 33.03288, 33.40792, 34.36113, 35.05449, 35.78606, 36.39031, 37.22832, 37.82788, 38.34854, 39.00118, 39.74676, 40.20306, 40.99312, 41.67428, 42.18971, 42.76524, 43.89556, 44.58645, 44.92146, 45.51138, 46.09642, 47.16946, 47.60448, 48.15453, 49.24764, 49.91994, 50.56865, 51.14569, 51.71552, 52.27938, 53.19557, 53.60767, 54.53672, 55.05678, 55.90673, 56.51751, 56.76284, 57.48033, 58.11004, 58.86049, 59.55114, 60.14212, 61.26292, 61.68166, 62.13097, 62.75237, 63.80856, 64.51841, 64.92895, 65.67979, 66.47918, 66.79789, 67.91478, 68.32424, 68.96133, 69.45491, 70.46093, 71.14826, 71.55111, 72.38623, 72.92412, 73.45081, 74.59989, 75.25102, 75.90003, 76.39067, 77.17377, 77.93056, 78.46454, 78.78206, 79.53754, 80.32568, 81.25387, 81.87898, 82.21593, 82.92279, 83.85489, 84.08421, 84.74823, 85.61222, 86.59029, 87.06243, 87.58542, 88.43858, 89.05994, 89.77241, 90.49294, 90.74067, 91.49063, 92.21, 93.16413, 93.54145, 94.54024, 95.12255, 95.74285, 96.49958, 97.00485, 97.69098, 98.34265, 99.23205, 99.62548]

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
p0 = 0.00123
birth_rate = 0.02158
death_rate = 0.00997
rebel_rate = 0.15915


'''