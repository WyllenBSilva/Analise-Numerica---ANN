import numpy as np
import math

#aa2bx

def best_poly(x, y, grau = 1):
    k = grau + 1
    A = [[0 for _ in range(k)] for _ in range(k)]
    B = [sum(y)]
    n = len(x)
    cache = {}
    for i in range(k):
        for j in range(k):
            p = i + j
            if (p == 0):
                A[0][0] = n
                continue
            if p not in cache:
                cache[p] = sum([xi ** p for xi in x])
            A[i][j] = cache[p]
        if i > 0:
            B.append(sum([yi * xi ** i for xi, yi in zip(x, y)]))
    return np.linalg.solve(A, B)

def poly(x, a, b):
    return a * math.pow(2,b*x)

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp

if __name__ == '__main__':

    x = [0.0322, 0.0687, 0.1423, 0.192, 0.2424, 0.3244, 0.3391, 0.3983, 0.45, 0.5222, 0.6031, 0.6281, 0.674, 0.7716, 0.8218, 0.8823, 0.9232, 0.9479, 1.0222, 1.0594, 1.1619, 1.2185, 1.2318, 1.3077, 1.3656, 1.4258, 1.4521, 1.5111, 1.6029, 1.6485, 1.7047, 1.7748, 1.7793, 1.8527, 1.9353, 1.9493]
    y = [5.0408, 4.9365, 6.3117, 5.2525, 5.6585, 6.4308, 6.2075, 6.2332, 7.0736, 7.2592, 8.9534, 9.2728, 8.4198, 8.5823, 10.1254, 11.481, 13.2619, 11.6211, 13.8811, 13.5015, 14.6231, 15.4214, 17.8133, 17.7789, 16.0977, 19.5173, 20.7505, 20.4417, 23.8893, 25.6968, 26.5952, 29.3773, 30.2599, 32.0984, 34.819, 32.4316]
    values = [0.3255, 1.0181, 1.3343, 1.4232, 1.8487]
    y_ = np.log(y)

    grau = 1

    a0, a1 = best_poly(x, y_, grau)

    #print(f'{a0 = } e {a1 = }')

    # ln(a) = a0 --> e^a0 = a
    a = np.exp(a0)

    #2^bx = a1 --> ln(2^bx) = ln(a1)  --> 
    # desconsidere o ln de "ln(a1)" --> ln(2^bx) = a1 --> 
    # b*x * ln(2) = a1 --> desconsidere x
    # b = a1/ln(2)
    b = a1/np.log(2)

    print(a,',',b,',')

    p = build_func(a, b)
    
    for xi_v in values:
        print(p(xi_v),',')
