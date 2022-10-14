#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#define L 3
#define C 3

double determinante(double matriz[L][C]){
    return (matriz[0][0]*matriz[1][1]*matriz[2][2]) + (matriz[0][1]*matriz[1][2]*matriz[2][0]) + (matriz[0][2]*matriz[1][0]*matriz[2][1]) - ((matriz[0][1]*matriz[1][0]*matriz[2][2]) + (matriz[0][0]*matriz[1][2]*matriz[2][1]) + (matriz[0][2]*matriz[1][1]*matriz[2][0]));
}

int main() {  
    double g = 9.81; 
    double v = 5.62; //<<<< ALTERAR O VALOR DA VELOCIDADE

    double m1, m2,m3, c1,c2,c3;

    m1 = 76.81, c1 = 9.12;
    m2 = 67.37, c2 = 14.68;
    m3 = 54.69, c3 = 18.84;
    // m1*g - T -c1*v = m1*a
    // m2*g + T - c2*v - R = m2*a
    // m3*g - c3*V + R = m3*a

    double R3 = c3*v - m3*g ;
    m3 *= -1;
    printf("\nequacao 1:   R %.2f*a + 0*T= %.16f",m3,R3);

    double R2 = c2*v - m2*g;
    m2 *= -1;
    printf("\nequacao 2:   -R %.2f*a + T= %.16f",m2,R2);

    double R1 = c1*v - m1*g;
    m1 *= -1;
    printf("\nequacao 3:   0R %.2f -T = %.16f",m1,R1);

    printf("\n\nMatriz Delta: \n");
    printf("1 %.4f 0\n",m3);
    printf("-1 %.4f 1\n",m2);
    printf("0 %.4f -1\n",m1);

    double Delta[L][C] = {
        {1,m3,0},
        {-1,m2,1},
        {0,m1,-1}
    };


    double detAlpha = determinante(Delta); //<-- cole aqui
    printf("DetAlpha = %.16f",detAlpha);

    printf("\n\n****Matriz Delta 1***:\n\n");
    printf("%.4f %.4f 0\n",R3,m3);
    printf("%.4f %.4f 1\n",R2,m2);
    printf("%.4f %.4f -1\n",R1,m1);
    double Delta1[L][C]={
        {R3, m3, 0},
        {R2, m2, 1},
        {R1, m1, -1}
    };          

    double det1 = determinante(Delta1); 
    printf("Det1 = %.16f\n",det1);

    printf("\n\n****Matriz Delta 2***:\n");
    printf("1 %.4f 0\n",R3);
    printf("-1 %.4f 1\n",R2);
    printf("0 %.4f -1\n",R1);

    double Delta2[L][C]={
        {1,R3, 0},
        {-1,R2, 1},
        {0,R1, -1}
    };  

    double det2 = determinante(Delta2); 
    printf("Det2 = %.16f\n",det2);

    printf("\n\n****Matriz Delta 3***:\n");
    printf("1 %.4f 0\n",m3);
    printf("-1 %.4f 1\n",m2);
    printf("0 %.4f -1\n",m1);

    double Delta3[L][C]={
        {1,m3,R3},
        {-1,m2,R2},
        {0,m1,R1},
    };


    double det3 = determinante(Delta3); //<-- cole aqui, coloque .0 na divisao
    printf("\ndet 3 = %.16f\n",det3);
    
    double a = det2/detAlpha;
    double R = det1/detAlpha;
    double T = det3/detAlpha;
    printf("a = %.16f\n",a);
    printf("R = %.16f\n",R);
    printf("T = %.16f\n",T);


    printf("\n****SOLUCAO****: \n\n");

    printf("\n\n%.16f, %.16f, %.16f\n\n",a,R,T);



    return 0;
}

