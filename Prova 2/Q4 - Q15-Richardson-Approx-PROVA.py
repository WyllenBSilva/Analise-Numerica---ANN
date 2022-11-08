import math

def richardson(x):
    n = len(x)
    for k in range(1, n):
        for i in range(n-k):
            numer = 2 ** k * x[i+1] - x[i]
            denom = 2 ** k - 1
            aprox = numer / denom
            x[i] = aprox
    return x[0]

if __name__ == '__main__':

    
    x0 = 2.7349
    approximations = [-0.15078737410798615, -0.11126498954339947, -0.09164195804311248, -0.08190197843850555]

    approx = richardson(approximations)

    print(f'{approx}, ')


    