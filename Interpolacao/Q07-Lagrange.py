def lagrange(x,y):
    #retorna yi dividido pelo denominador do polinomio Li
    num=len(x)
    coefs = []
    for i in range(num):
        prod=1
        for j in range(num):
            if i!=j:
                prod*=(x[i] - x[j])
        ci=y[i]/prod
        coefs.append(ci)
    return coefs

def pl(t,x,coefs) -> float:
    soma=0
    num = len(coefs)
    for i in range(num):
        prod=1
        for j in range(num):
            if i!=j:
                prod*=(t-x[j])
        prod*= coefs[i]
        soma+=prod
    return soma


def poly(x, coefs):
    def f(t):
        return pl(t,x, coefs)
    return f


if __name__ == '__main__':
    #x = [1.114, 2.139, 3.22]
    #y = [1.54, 1.754, 0.109]

    #x = [2.663, 2.967, 3.182, 3.412, 3.653, 4.06, 4.309, 4.574]
    #y = [0.639, 0.788, 0.852, 0.904, 0.949, 0.999, 0.967, 0.278]

    x = [0.351, 0.667, 1.444, 1.917, 2.698, 3.039, 4.023, 4.379, 5.108, 5.757, 6.163, 6.61]
    y = [4.823, 4.427, 3.251, 2.686, 2.097, 2.005, 2.364, 2.673, 3.385, 3.865, 3.993, 3.947]
    
    # x=[-0.691, 0.247, 0.681]
    # y=[0.07729752396, 0.39600431644 ,0.07940273264]
    
    # x=[1,3]
    # y=[1,-1]
    c = lagrange(x,y)
    print(c)
    lagr=poly(x, c)
    # print(lagrange(x, y))
    #print(lagr(0))