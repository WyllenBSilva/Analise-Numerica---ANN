import math

p0 = 0.00143
birth_rate = 0.02804
death_rate = 0.00949
rebel_rate = 0.1562

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



t_values = [0.37485, 1.25089, 1.50651, 2.45218, 3.21029, 3.82616, 4.15828, 4.93979, 5.60094, 6.27996, 6.83326, 7.55669, 8.38688, 8.8599, 9.89446, 10.21177, 11.1426, 11.58954, 12.35632, 12.96534, 13.50284, 14.42628, 15.13295, 15.42868, 16.0713, 16.80453, 17.72445, 18.15397, 18.73944, 19.72928, 20.46358, 21.05463, 21.59168, 22.38162, 23.20887, 23.79657, 24.38988, 25.03032, 25.41945, 26.31347, 27.21978, 27.80699, 28.38928, 29.09942, 29.57478, 30.56929, 30.99982, 31.73182, 32.39536, 33.03674, 33.61137, 34.10125, 34.75849, 35.83225, 36.50861, 37.07137, 37.43699, 38.25719, 38.94301, 39.55815, 40.5196, 41.11235, 41.81718, 42.26934, 43.19595, 43.46362, 44.21188, 45.21762, 45.62419, 46.383, 46.83976, 47.54795, 48.36159, 49.25653, 49.55725, 50.19524, 51.07171, 51.87537, 52.49227, 52.79863, 53.682, 54.25857, 55.20715, 55.80524, 56.5517, 56.85209, 57.44381, 58.30041, 58.95308, 59.58642, 60.45615, 60.75774, 61.74914, 62.44782, 63.13265, 63.92715, 64.3814, 64.81255, 65.81398, 66.41772, 67.09306, 67.48258, 68.08263, 69.02894, 69.77929, 70.49513, 70.74439, 71.58333, 72.47242, 73.04042, 73.82655, 74.11391, 75.2663, 75.5551, 76.54144, 77.01385, 77.45449, 78.56972, 78.78357, 79.71041, 80.59657, 81.0026, 81.55198, 82.13993, 83.18468, 83.88697, 84.10748, 85.21442, 85.53517, 86.07142, 86.99537, 87.63133, 88.38556, 88.75905, 89.82904, 90.25495, 90.82928, 91.82622, 92.10212, 92.85984, 93.45286, 94.20234, 94.87391, 95.90279, 96.08388, 96.79687, 97.47183, 98.23572, 99.2201, 99.51189]

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