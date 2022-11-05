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

    

    def f(x):
        return x ** (x ** -x)

    h = 0.39691
    x0 = 1.73576
    orders = [4, 5, 6, 7, 8]

    def F1(h):
        return (f(x0 + h) - f(x0)) / h


    for i in range(len(orders)):
        col_F1 = [F1(h/2**i) for i in range(orders[i])]
        approx = richardson(col_F1)

        print(f'{approx}, ')

    richardson(col_F1)


    #col_F1 =[F1(h),F1(h/2),F1(h/4),F1(h/8),F1(h/16),F1(h/32)]

    #print(f'{col_F1 =} ')
    #aprox = richardson(col_F1)
    #print(f'Aprox para f\'({x0})~{aprox} com erro eh O(h^{len(col_F1)})')
    #print(f'{exato = }')
    