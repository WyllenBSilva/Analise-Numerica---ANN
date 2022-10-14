import numpy as np

def poly(x,y):
    n = len(x)-1
    A =[]
    B =[]
    for xi in x:
        row = [1]
        for j in range(1, n+1):
            row.append(xi ** j)
        A.append(row)
    return np.linalg.solve(A, y)

def func_poly(x, coeffs):
    first=coeffs[0]
    return first + sum([ai * x ** j for j, ai in enumerate(coeffs[1:], 1)])

if __name__ == '__main__':
    #exemplo 1

    x = [0.5, 0.793, 1.643, 2.193, 2.414, 3.433, 3.743, 4.348, 4.749, 5.386, 6.046, 6.887]
    y = [4.471, 4.691, 4.907, 4.652, 4.471, 3.32, 2.967, 2.435, 2.249, 2.251, 2.547, 2.987]

    coeffs = poly(x,y)
    #print(coeffs)

    for x in (coeffs):
        print("%.16f," %x)
    def p(x):
        return func_poly(x,coeffs)

#    print("%.16f" %p(4.879))
 #   print("%.16f" %p(5.113))
  #  print("%.16f" %p(5.202))




#visulaizar
#import matplotlib.pylab as plt

#plt.scatter(x,y)
#t = np.linspace(min(x),  max(x), 200)
#pt = [p(ti) for ti in t]

#função seno
# st=np.sin(t)
# plt.plot(t, pt)
# plt.plot(t, st)

#plt.plot(t, pt)
#plt.savefig('interp.png')

