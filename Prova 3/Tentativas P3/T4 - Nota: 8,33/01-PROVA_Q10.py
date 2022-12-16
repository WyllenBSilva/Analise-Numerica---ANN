import math
import numpy as np

'''
Seja Pn(x) o polinômio de Legendre de grau n. Encontre os coeficientes da combinação linear
g(x)=∑k=050ckPk(x)
que melhor se aproxima da função f(x)=ln(1+x2)sin(10x) no intervalo [−1,1]. Para o cálculo dos coeficientes ck, use o método da quadratura gaussiana que seja exato em polinômios de grau menor que 24. Em seguida calcule g(x) para os seguintes valores de x,
x1=−0.884, x2=0.099 e x3=0.58.
A função g(x) é uma aproximação para a função f(x) no intervalo [−1,1] com erro dado por
erro=∫1−1[f(x)−g(x)]2dx.
Use a regra dos trapézios com 1024 subintervalos para determinar o erro.
'''
def trapz(f, a, b, h):
    n = int((b - a)/h)
    soma = 0
    for k in range(1, n):
        soma += f(a + k * h)
    soma *= 2
    soma += f(a) + f(b)
    soma *= h/2
    return soma


def simps(f, a, b, n):
    if n % 2 != 0:
        print('O valor n deve ser par')
        return None

    num_parabolas = n / 2
    soma = 0
    h = (b - a) / n

    for i in range(int(num_parabolas)):
        x0 = a + (2 * i) * h
        x1 = a + (2 * i + 1) * h
        x2 = a + (2 * i + 2) * h
        soma += f(x0) + 4 * f(x1) + f(x2)

    soma *= h / 3

    return soma


def trapz_romberg(f, a, b, h):
    n = int((b - a) / h)
    soma = 0

    for k in range(1, n):
        soma += f(a + k * h)

    return (h / 2) * (f(a) + 2 * soma + f(b))


def romberg(coluna_f1):
    coluna_f1 = [i for i in coluna_f1]
    n = len(coluna_f1)
    for j in range(n - 1):
        temp_col = [0] * (n - 1 - j)
        for i in range(n - 1 - j):
            power = j + 1
            temp_col[i] = (4 ** power * coluna_f1[i + 1] - coluna_f1[i]) / (4 ** power - 1)
        coluna_f1[:n - 1 - j] = temp_col
        # print(f'F_{j+2} = {temp_col}')
    return coluna_f1[0]


def best_func(f, funcs, a, b, method: ['trapz', 256]):
    k = len(funcs)

    A = [[0 for _ in range(k)] for _ in range(k)]
    B = []

    for i in range(k):
        for j in range(k):
            if i == j:
                if j >= i:
                    def f_ij(x):
                        return funcs[j](x) * funcs[i](x)

                    if method[0] == 'trapz':
                        A[i][j] = trapz(f_ij, a, b, method[1])
                    elif method[0] == 'simps':
                        A[i][j] = simps(f_ij, a, b, method[1])
                    elif method[0] == 'romberg':
                        tam = int(method[1] / 2)
                        hs = [method[2] / 2 ** ki for ki in range(tam)]
                        coluna_f1 = [trapz_romberg(f_ij, a, b, hi) for hi in hs]
                        A[i][j] = romberg(coluna_f1)
                    elif method[0] == 'quadratura':
                        A[i][j] = quadratura(change(f_ij, a, b), method[1], method[2])

                else:
                    A[i][j] = A[j][i]

        def ffi(x):
            return f(x) * funcs[i](x)

        if method[0] == 'trapz':
            B.append(trapz(ffi, a, b, method[1]))
        elif method[0] == 'simps':
            B.append(simps(ffi, a, b, method[1]))
        elif method[0] == 'romberg':
            tam = int(method[1] / 2)
            hs = [method[2] / 2 ** ki for ki in range(tam)]
            coluna_f1 = [trapz_romberg(ffi, a, b, hi) for hi in hs]
            B.append(romberg(coluna_f1))
        elif method[0] == 'quadratura':
            B.append(quadratura(change(ffi, a, b), method[1], method[2]))

    A = np.array(A, dtype=float)
    B = np.array(B, dtype=float)

    return np.linalg.solve(A, B)


def quadratura(funcao, pontos, pesos):
    soma = 0

    for xk, ck in zip(pontos, pesos):
        soma += ck * funcao(xk)

    return soma


def change(f, a, b):
    def g(u):
        return f((b + a) / 2 + (b - a) * u / 2) * (b - a) / 2

    return g


def legendre(x, n):
    f0 = 1.0
    f1 = x
    fn = 0

    ni = 2

    if n == 0:
      return 1.0

    elif n == 1:
      return x

    else:

      while ni <= n:
          fn = ((2* ni - 1) * x * f1 - (ni - 1) * f0) / ni
          f0 = f1
          f1 = fn
          ni += 1 

    return fn

def build_legendre_polynomial(n):
    def temp(t):
        return legendre(t, n)

    return temp

def f(x):
    return math.log(1 + x**2) * math.sin(10 * x)



if __name__ == '__main__':
    
    raiz2 = [-0.5773502691896257, 0.5773502691896257]
    peso2 = [1.0, 1.0]

    raiz3 = [0, -0.7745966692414834, 0.7745966692414834]
    peso3 = [0.8888888888888888, 0.5555555555555556, 0.5555555555555556]

    raiz4 = [-0.33998104358485626, 0.33998104358485626, -0.8611363115940526, 0.8611363115940526]
    peso4 = [0.6521451548625461, 0.6521451548625461, 0.34785484513745385, 0.34785484513745385]

    raiz5 = [0, -0.5384693101056831, 0.5384693101056831, -0.906179845938664, 0.906179845938664]
    peso5 = [0.5688888888888889, 0.47862867049936647, 0.47862867049936647, 0.23692688505618908, 0.23692688505618908]

    raiz6 = [0.6612093864662645, -0.6612093864662645, -0.2386191860831969, 0.2386191860831969, -0.932469514203152,
             0.932469514203152]
    peso6 = [0.3607615730481386, 0.3607615730481386, 0.46791393457269104, 0.46791393457269104, 0.17132449237917036,
             0.17132449237917036]

    raiz7 = [0, 0.4058451513773972, -0.4058451513773972, -0.7415311855993945, 0.7415311855993945, -0.9491079123427585,
             0.9491079123427585]
    peso7 = [0.4179591836734694, 0.3818300505051189, 0.3818300505051189, 0.27970539148927664, 0.27970539148927664,
             0.1294849661688697, 0.1294849661688697]

    raiz8 = [-0.1834346424956498, 0.1834346424956498, -0.525532409916329, 0.525532409916329, -0.7966664774136267,
             0.7966664774136267, -0.9602898564975363, 0.9602898564975363]
    peso8 = [0.362683783378362, 0.362683783378362, 0.31370664587788727, 0.31370664587788727, 0.22238103445337448,
             0.22238103445337448, 0.10122853629037626, 0.10122853629037626]

    raiz9 = [0, -0.8360311073266358, 0.8360311073266358, -0.9681602395076261, 0.9681602395076261, -0.3242534234038089,
             0.3242534234038089, -0.6133714327005904, 0.6133714327005904]
    peso9 = [0.3302393550012598, 0.1806481606948574, 0.1806481606948574, 0.08127438836157441, 0.08127438836157441,
             0.31234707704000286, 0.31234707704000286, 0.26061069640293544, 0.26061069640293544]

    raiz10 = [-0.14887433898163122, 0.14887433898163122, -0.4333953941292472, 0.4333953941292472, -0.6794095682990244,
              0.6794095682990244, -0.8650633666889845, 0.8650633666889845, -0.9739065285171717, 0.9739065285171717]
    peso10 = [0.29552422471475287, 0.29552422471475287, 0.26926671930999635, 0.26926671930999635, 0.21908636251598204,
              0.21908636251598204, 0.1494513491505806, 0.1494513491505806, 0.06667134430868814, 0.06667134430868814]

    raiz11 = [0, -0.26954315595234496, 0.26954315595234496, -0.5190961292068118, 0.5190961292068118,
              -0.7301520055740494,
              0.7301520055740494, -0.8870625997680953, 0.8870625997680953, -0.978228658146057, 0.978228658146057]
    peso11 = [0.2729250867779006, 0.26280454451024665, 0.26280454451024665, 0.23319376459199048, 0.23319376459199048,
              0.18629021092773426, 0.18629021092773426, 0.1255803694649046, 0.1255803694649046, 0.05566856711617366,
              0.05566856711617366]

    raiz12 = [-0.1252334085114689, 0.1252334085114689, -0.3678314989981802, 0.3678314989981802, -0.5873179542866175,
              0.5873179542866175, -0.7699026741943047, 0.7699026741943047, -0.9041172563704749, 0.9041172563704749,
              -0.9815606342467192, 0.9815606342467192]
    peso12 = [0.24914704581340277, 0.24914704581340277, 0.2334925365383548, 0.2334925365383548, 0.20316742672306592,
              0.20316742672306592, 0.16007832854334622, 0.16007832854334622, 0.10693932599531843, 0.10693932599531843,
              0.04717533638651183, 0.04717533638651183]

    raiz13 = [0, -0.2304583159551348, 0.2304583159551348, -0.44849275103644687, 0.44849275103644687,
              -0.6423493394403402,
              0.6423493394403402, -0.8015780907333099, 0.8015780907333099, -0.9175983992229779, 0.9175983992229779,
              -0.9841830547185881, 0.9841830547185881]
    peso13 = [0.2325515532308739, 0.22628318026289723, 0.22628318026289723, 0.2078160475368885, 0.2078160475368885,
              0.17814598076194574, 0.17814598076194574, 0.13887351021978725, 0.13887351021978725, 0.09212149983772845,
              0.09212149983772845, 0.04048400476531588, 0.04048400476531588]

    raiz14 = [-0.10805494870734367, 0.10805494870734367, -0.31911236892788974, 0.31911236892788974, -0.5152486363581541,
              0.5152486363581541, -0.6872929048116855, 0.6872929048116855, -0.827201315069765, 0.827201315069765,
              -0.9284348836635735, 0.9284348836635735, -0.9862838086968123, 0.9862838086968123]
    peso14 = [0.2152638534631578, 0.2152638534631578, 0.2051984637212956, 0.2051984637212956, 0.18553839747793782,
              0.18553839747793782, 0.15720316715819355, 0.15720316715819355, 0.12151857068790319, 0.12151857068790319,
              0.08015808715976021, 0.08015808715976021, 0.03511946033175186, 0.03511946033175186]

    raiz15 = [0, -0.20119409399743451, 0.20119409399743451, -0.3941513470775634, 0.3941513470775634,
              -0.5709721726085388,
              0.5709721726085388, -0.7244177313601701, 0.7244177313601701, -0.8482065834104272, 0.8482065834104272,
              -0.937273392400706, 0.937273392400706, -0.9879925180204854, 0.9879925180204854]
    peso15 = [0.2025782419255613, 0.19843148532711158, 0.19843148532711158, 0.1861610000155622, 0.1861610000155622,
              0.16626920581699392, 0.16626920581699392, 0.13957067792615432, 0.13957067792615432, 0.10715922046717194,
              0.10715922046717194, 0.07036604748810812, 0.07036604748810812, 0.03075324199611727, 0.03075324199611727]

    raiz16 = [-0.09501250983763744, 0.09501250983763744, -0.2816035507792589, 0.2816035507792589, -0.45801677765722737,
              0.45801677765722737, -0.6178762444026438, 0.6178762444026438, -0.755404408355003, 0.755404408355003,
              -0.8656312023878318, 0.8656312023878318, -0.9445750230732326, 0.9445750230732326, -0.9894009349916499,
              0.9894009349916499]
    peso16 = [0.1894506104550685, 0.1894506104550685, 0.18260341504492358, 0.18260341504492358, 0.16915651939500254,
              0.16915651939500254, 0.14959598881657674, 0.14959598881657674, 0.12462897125553388, 0.12462897125553388,
              0.09515851168249279, 0.09515851168249279, 0.062253523938647894, 0.062253523938647894,
              0.027152459411754096,
              0.027152459411754096]

    raiz17 = [0, -0.17848418149584785, 0.17848418149584785, -0.3512317634538763, 0.3512317634538763,
              -0.5126905370864769,
              0.5126905370864769, -0.6576711592166907, 0.6576711592166907, -0.7815140038968014, 0.7815140038968014,
              -0.8802391537269859, 0.8802391537269859, -0.9506755217687678, 0.9506755217687678, -0.9905754753144174,
              0.9905754753144174]
    peso17 = [0.17944647035620653, 0.17656270536699264, 0.17656270536699264, 0.16800410215645004, 0.16800410215645004,
              0.15404576107681028, 0.15404576107681028, 0.13513636846852548, 0.13513636846852548, 0.11188384719340397,
              0.11188384719340397, 0.08503614831717918, 0.08503614831717918, 0.0554595293739872, 0.0554595293739872,
              0.02414830286854793, 0.02414830286854793]

    raiz18 = [-0.0847750130417353, 0.0847750130417353, -0.2518862256915055, 0.2518862256915055, -0.41175116146284263,
              0.41175116146284263, -0.5597708310739475, 0.5597708310739475, -0.6916870430603532, 0.6916870430603532,
              -0.8037049589725231, 0.8037049589725231, -0.8926024664975557, 0.8926024664975557, -0.9558239495713977,
              0.9558239495713977, -0.9915651684209309, 0.9915651684209309]
    peso18 = [0.1691423829631436, 0.1691423829631436, 0.16427648374583273, 0.16427648374583273, 0.15468467512626524,
              0.15468467512626524, 0.14064291467065065, 0.14064291467065065, 0.12255520671147846, 0.12255520671147846,
              0.10094204410628717, 0.10094204410628717, 0.07642573025488905, 0.07642573025488905, 0.0497145488949698,
              0.0497145488949698, 0.02161601352648331, 0.02161601352648331]

    raiz19 = [0, -0.16035864564022537, 0.16035864564022537, -0.31656409996362983, 0.31656409996362983,
              -0.46457074137596094,
              0.46457074137596094, -0.600545304661681, 0.600545304661681, -0.7209661773352294, 0.7209661773352294,
              -0.8227146565371428, 0.8227146565371428, -0.9031559036148179, 0.9031559036148179, -0.96020815213483,
              0.96020815213483, -0.9924068438435844, 0.9924068438435844]
    peso19 = [0.1610544498487837, 0.15896884339395434, 0.15896884339395434, 0.15276604206585967, 0.15276604206585967,
              0.1426067021736066, 0.1426067021736066, 0.12875396253933621, 0.12875396253933621, 0.11156664554733399,
              0.11156664554733399, 0.09149002162245, 0.09149002162245, 0.06904454273764123, 0.06904454273764123,
              0.0448142267656996, 0.0448142267656996, 0.019461788229726478, 0.019461788229726478]

    raiz20 = [-0.07652652113349734, 0.07652652113349734, -0.22778585114164507, 0.22778585114164507,
              -0.37370608871541955,
              0.37370608871541955, -0.5108670019508271, 0.5108670019508271, -0.636053680726515, 0.636053680726515,
              -0.7463319064601508, 0.7463319064601508, -0.8391169718222188, 0.8391169718222188, -0.912234428251326,
              0.912234428251326, -0.9639719272779138, 0.9639719272779138, -0.9931285991850949, 0.9931285991850949]
    peso20 = [0.15275338713072584, 0.15275338713072584, 0.14917298647260374, 0.14917298647260374, 0.14209610931838204,
              0.14209610931838204, 0.13168863844917664, 0.13168863844917664, 0.11819453196151841, 0.11819453196151841,
              0.10193011981724044, 0.10193011981724044, 0.08327674157670475, 0.08327674157670475, 0.06267204833410907,
              0.06267204833410907, 0.04060142980038694, 0.04060142980038694, 0.017614007139152118, 0.017614007139152118]

    grau = 51
    subintervalo_para_erro = 1024
    funcs = [build_legendre_polynomial(i) for i in range(grau)]
    a = -1
    b = 1
    
    x1=-0.448
    x2=0.011 
    x3=0.415
    

    values = [x1,x2,x3]
    # quadratura gaussina
    exact_for_degree_less_than = 24
    order = str(int(exact_for_degree_less_than / 2))
    txt_order = ['raiz' + order, 'peso' + order]
    method = ['quadratura', locals()[txt_order[0]], locals()[txt_order[1]]]


    coefs = best_func(f, funcs, a, b, method)

    coefs = [ci for ci in coefs]

    for i in coefs:
        print(f'{i}, ')

    def g(x):
        return sum(ci * fi(x) for ci, fi in zip(coefs, funcs))


    for x in values:
        print(f'{g(x)}, ')



    def func_erro(x):
        return (f(x) - g(x)) ** 2


    erro = trapz(func_erro, a, b, subintervalo_para_erro)

    print(f'{erro}')