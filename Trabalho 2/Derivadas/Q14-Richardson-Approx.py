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

    
    x0 = 3.77814
    approximations = [0.2245242787395254, 0.2174295447528447, 0.21376125179216388]


    approx = richardson(approximations)

    print(f'{approx}, ')


    