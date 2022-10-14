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
                printf("atingiu a tolerancia em F(Mk)=> x_%d = %.16f\n",i+1,m);
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

bissectionIntervalo(double (*f)(double),double a,double b, int n, double tol) {
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
            if(fabs(b-a)<tol) {
                printf("atingiu a tolerancia no Intervalo => x_%d = %.16f\n",i+1,m);
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
    return log((x*x))-0.7;
}



int main() {

    double a = 0.88;
    double b = 2.9499;

    

    //int n = 4;
    //int n = 8;
    //int n = 11;
    //int n = 15;
    int n = 39;
    
    double tol = 0.000000000000000000001;

    bissection(f,a,b,n,tol);

    printf("\n\n");

    bissectionIntervalo(f,a,b,n,tol);

    return 0;
}