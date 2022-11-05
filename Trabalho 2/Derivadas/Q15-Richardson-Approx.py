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

    
    x0 = 0.0242
    approximations = [-0.16269560523700122, -0.04930665890658581, 0.0008719165410440155, 0.024309226218157676, 0.03561423487610682, 0.04116337337214304]


    approx = richardson(approximations)

    print(f'{approx}, ')


    