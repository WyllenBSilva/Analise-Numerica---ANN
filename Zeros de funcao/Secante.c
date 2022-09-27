#include <stdio.h>
#include <math.h>

void secante (double (*f)(double),double x0,double x1,int n ) {

    for(int i = -1;i<n;i++) {
        double fx0 = f(x0);
        double fx1 = f(x1);
        if(fx0 == fx1) {
            break;
        }
        double x2 = (x0*fx1-x1*fx0) / (fx1-fx0);
        printf("x_%d = %.16f\n",i+2,x2);
        x0 = x1;
        x1 = x2;
    }
}
double f(double x) {
    //return 2*asin(1.0)*x-exp(x);
    //return 2*(x+1)*(x-0.5)*(x-1);
    return (((2*asin(1.0)*8.59)/3)*(pow(2.0,2)+pow(7.73,2)+2.0*7.73))*599.17-1000*((2*asin(1.0)*(8.59-x))/3)*(pow(2.0,2)+pow(7.73,2)+2.0*7.73);
}

int main () {

    double x0 = 1.27;
    double x1 = 7.51;

    int n = 5;

    secante(f,x0,x1,n);


    return 0;
}