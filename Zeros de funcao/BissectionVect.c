#include <stdio.h>
#include <math.h>

bissection(double (*f)(double),double a,double b, int n, double tol) {
    double fa = f(a);
    double fb = f(b);

    if(fa*fb >=0) {
        printf("voce nao pode usar esse intervalo");
        return;
    } else {
        for(int i=0;i<n;i++) {
            double m = 0.5*(a+b);
            double fm = f(m);

            if(fabs(fm) ==0) {
                printf("voce encontrou uma raiz r= %.16f",fm);
                return;
            }

            printf("x_%d = %.16f\n",i+1,m);

            if(fabs(fm)<tol) {
                printf("atingiu a tolerancia => x_%d = %.16f\n",i+1,m);
                return;
            }
            if(fa*fm<0) {
                b = m;
            } else {
                a = m;
            }

            

        }
    }
}

bissectionvec(double (*f)(double),double a,double b, int n, double tol, int vec[]) {
    int j = 0;
    double fa = f(a);
    double fb = f(b);

    if(fa*fb >=0) {
        printf("voce nao pode usar esse intervalo");
        return;
    } else {
        for(int i=1;i<=n;i++) {
            double m = 0.5*(a+b);
            double fm = f(m);

            if(fabs(fm) ==0) {
                printf("voce encontrou uma raiz r= %.16f",fm);
                return;
            }

            
            if(i == vec[j]){
                printf("%.16f, ",m);
                j++;
            }
            

            if(fabs(fm)<tol) {
                printf("atingiu a tolerancia => x_%d = %.16f\n",i+1,m);
                return;
            }
            if(fa*fm<0) {
                b = m;
            } else {
                a = m;
            }

            

        }
    }
}




double f(double x) {
    //return x*x-3.2615 * x + 1.1391;
    return exp(x)-2*(pow(x,2)) + x - 1.5;
}

int main() {

    //int vec[100] = {2, 3, 6, 7, 8, 9, 10, 15, 16, 19, 22, 23, 27, 28, 29, 30, 32, 36, 38, 39};
    //int vec[4] = {2, 4, 5, 6};
    int vec[100] = {2, 4, 8, 12};

    //double a =  1.5926;
    //double b = 5.0989;

    //double a =  1.93434;
    //double b = 2.74022;
    
    double a = 0.1;
    double b = 1.25;
    

    //int n = 4;
    //int n = 8;
    //int n = 11;
    //int n = 15;
    //int n = 7;
    int n = 12;
    
    double tol = 0.0000000000001;

    bissection(f,a,b,n,tol);
    printf(" \n Valor em vetor: \n");

    bissectionvec(f,a,b,n,tol,vec);

    return 0;
}