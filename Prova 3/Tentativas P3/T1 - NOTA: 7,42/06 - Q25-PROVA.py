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
    rebel_rate = 0.16784
    birth_rate = 0.01721
    k = rebel_rate * birth_rate
    return k * (1 - t)

# modificar valor de p0

''''
t0 = 0
p0 = 0.00179




'''
t0 = 0
p0 = 0.00179

t_values = [0.11996, 1.16003, 1.64082, 2.2422, 2.88225, 3.49742, 4.10999, 5.25008, 5.63452, 6.22712, 7.04881, 7.90182, 8.29523, 8.97967, 9.64585, 10.46271, 11.20437, 11.77916, 12.16187, 12.92194, 13.75349, 14.48351, 15.12969, 15.9286, 16.13926, 17.25242, 17.9052, 18.10199, 18.78476, 19.71806, 20.13771, 20.96846, 21.78294, 22.393, 23.05685, 23.65522, 24.24772, 24.93193, 25.59633, 26.41364, 27.03266, 27.89708, 28.22376, 29.09027, 29.56996, 30.29965, 30.75412, 31.60691, 32.38459, 33.15935, 33.51785, 34.20114, 35.17387, 35.85709, 36.10304, 37.00735, 37.49578, 38.32471, 39.12589, 39.91763, 40.29878, 41.2542, 41.62535, 42.59419, 42.84792, 43.71977, 44.55078, 44.86617, 45.74656, 46.17071, 46.78671, 47.85811, 48.57393, 49.25945, 49.47082, 50.28867, 51.01302, 51.91994, 52.54161, 53.13433, 53.43985, 54.1326, 55.11902, 55.80973, 56.49919, 56.77165, 57.80622, 58.3698, 58.86611, 59.48094, 60.29278, 61.04553, 61.89683, 62.48534, 63.05792, 63.51621, 64.13792, 64.87231, 65.64408, 66.17659, 66.90773, 67.70775, 68.30306, 68.74863, 69.64623, 70.32581, 70.82796, 71.85137, 72.15017, 73.18227, 73.70171, 74.52435, 74.76179, 75.74301, 76.39879, 76.98369, 77.69433, 78.36341, 78.90285, 79.77415, 80.36088, 80.81402, 81.54413, 82.27693, 83.2605, 83.86659, 84.42678, 84.76167, 85.44419, 86.40923, 86.92448, 87.48001, 88.31945, 89.12076, 89.49881, 90.45062, 90.91961, 91.82956, 92.12779, 93.00859, 93.75605, 94.2662, 95.00169, 95.83021, 96.10308, 97.17566, 97.48013, 98.54908, 99.15469, 99.81305]

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
    rebel_rate = 0.16784
    birth_rate = 0.01721
    k = rebel_rate * birth_rate
    # resolver:
    # solve p'(t) = k * (1 - p(t)), p(0) = p0
    # no wolfram, substituindo o valor de p0 dado na questao, então:
    #solve p'(t) = k * (1 - p(t)), p(0) = 0.00179
    death_rate = 0.00507

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
p0 = 0.00134
birth_rate = 0.01721
death_rate = 0.00507
rebel_rate = 0.16784

'''