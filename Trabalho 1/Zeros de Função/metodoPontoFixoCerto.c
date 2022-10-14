#include <stdio.h>
#include <math.h>

void fixed_point(double (*g)(double),double x0, int n) {
    for(int i = 0;i<n;i++) {
        x0 = g(x0);
        printf("x_%d = %.16f\n",i+1,x0);
    }
    
}

void fixed_pointVECT(double (*g)(double),double x0, int n, int vec[]) {
    printf("\nValor em vetor: \n\n");
    int j = 0;
    for(int i = 0;i<n;i++) {
        x0 = g(x0);
        if(i+1==vec[j]) {
            printf("%.16f,\n",x0);
            j++;
        }
        
    }
    
}
//nao usa f para nada
double g(double x) {
    return ((3 * pow(x, 4) + 2 * pow(x, 2) + 3) / (4 * pow(x, 3) + 4 * x - 1));
}

int main(){

    int n = 8;
    double x0 = 1.67175;
    int vec[100] = {1, 2, 3, 4, 5, 6, 7, 8};

    //quanto mais aumento o numero de interacoes, mais proximo chego do valor real

    fixed_point(g,x0,n);

    fixed_pointVECT(g,x0,n,vec);

    return 0;
}