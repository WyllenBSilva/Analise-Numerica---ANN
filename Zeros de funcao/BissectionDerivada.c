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

bissectionDerivada(double (*p)(double),double a,double b, int n) {
    double fa = p(a);
    double fb = p(b);

    if(fa*fb >=0) {
        printf("voce nao pode usar esse intervalo");
        return;
    } else {
        for(int i=0;i<n;i++) {
            double m = 0.5*(a+b);
            double fm = p(m);

            if(fabs(fm) ==0) {
                printf("voce encontrou uma raiz r= %.16f",fm);
                return;
            }
            printf("x_%d = %.16f\n",i+1,m);
            
            if(fa*fm<0) {
                b = m;
            } else {
                a = m;
            }

        }
    }
}


double f(double x) {
    return pow(x,3)-7*pow(x,2)+14*x-7;
}

//k -> lambda

double p(double k) {
    return 1161920 * exp(k) + (109945/k) * (exp(k)-1) - 2183290;
}


int main() {

    double a = 0.1;
    double b = 1.28;

    //int n = 4;
    //int n = 8;
    //int n = 11;
    //int n = 15;
    //int n = 65;
    int n = 12;
    
    //double tol = 4.61807e-11;

    //bissection(f,a,b,n,tol);

    printf("\n\n");

    //bissectionIntervalo(f,a,b,n,tol);

    bissectionDerivada(p,a,b,n);

    return 0;
}