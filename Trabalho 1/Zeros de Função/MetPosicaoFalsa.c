#include <stdio.h>

void PosicaoFalsa(double (*f)(double),double a,double b,int n ) {

    for(int i = 0;i<n;i++) {
        double fa = f(a);
        double fb = f(b);

        if(fa*fb >=0) {
            printf("o teorema de bolzano nao sabe dizer se existe raiz");
            break;
        }
        
        double x1 = (a*fb-b*fa) / (fb-fa);

        printf("x_%d = %.16f\n",i+1,x1);
        double fx1 = f(x1);
        if(fa*fx1 <0) {
            b = x1;
            fb = fx1;
        } else {
            a = x1;
            fa = fx1;
        }
    }
}

void PosicaoFalsaVECT(double (*f)(double),double a,double b,int n, int vec[]) {

    printf("\nValores em vetor: \n\n");

    int j=0;

    for(int i = 0;i<n;i++) {
        double fa = f(a);
        double fb = f(b);

        if(fa*fb >=0) {
            printf("o teorema de bolzano nao sabe dizer se existe raiz");
            break;
        }
        
        double x1 = (a*fb-b*fa) / (fb-fa);

        if(i+1==vec[j]) {
            printf("%.16f,\n",x1);
            j++;
        }
        
        double fx1 = f(x1);
        if(fa*fx1 <0) {
            b = x1;
            fb = fx1;
        } else {
            a = x1;
            fa = fx1;
        }
    }
}




double f(double x) {
    //return 2*asin(1.0)*x-exp(x);
    return exp(5*x)-2;
}

int main () {

    
    double a = -0.9753159;
    double b = 1.9415645;

    int n = 10000;

    int vec[100] = {1, 25, 50, 100, 200, 400, 800, 1600, 3200, 4800, 6400, 8000, 10000};

    //PosicaoFalsa(f,a,b,n);

    PosicaoFalsaVECT(f,a,b,n,vec);


    return 0;
}