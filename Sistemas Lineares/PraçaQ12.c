
#include <stdio.h>

int main() {

    /*
        k1=510, k2=673, k3=230, k4=345, k5=303 e  k6=1149

        PARA DENTRO
        k1 + k2 + k4 + k5 ==> 510+673+345+303 = 1831
        PARA FORA
        k3 + k6 + x ==> 230+1149+ x = 1379 + x

        1831 - 1379 = x 
        x = 452

        cruzamento  dentro  fora 
        A		K4+k5 = X2 + X3
        B		X3+K7 = K6 + x
        C       K1+K2 = K7 + x1
        D		X1+X2 = k3


        X2 + X3 = 648
                X3 = 682 - K7
        X1 			= 1183 - K7
        X1 + X2		= 1149


        682 - 648 = 34
        média de 330 veículos 

        X1 = 1149-330 + 34 = 853
        X2 = 1149-853 = 296
        X3 = 648 - 296 = 352
        X = 452

    */

    //Valores que eu mudo::::
    int k1=612, k2=630, k3=1051, k4=281, k5=335,  k6=268;
    int mediaDeVeiculos = 484;
    //Fim valores que mudo



    int x1, x2, x3,x;
    int PraDentro = k1+k2+k4+k5;
    int praFora = k3 + k6;
    x = PraDentro - praFora;

    printf("Valor de x: %d\n",x);

    printf("x2 + x3 = %d\n",k4+k5);
    printf("x3 = %d - K7\n",k6+x);
    printf("x1 = %d - K7\n",k1+k2);
    printf("x1 + x2 = %d\n",k3);


    int z = (k6+x)-(k4+k5);

    x1 = k3 - mediaDeVeiculos + z;
    x2 = k3 - x1;
    x3 = k4 + k5 - x2;

    printf("\n\n%d,%d,%d,%d\n\n\n",x,x1,x2,x3);


    return 0;
}