#include <stdio.h>
#include <math.h>

void newtonvec(double(*f)(double),double(*df)(double),double x0,int n, int vec[]) {
    int j = 0;
    for(int i =0;i<n;i++) {
        
        double dfx0 = df(x0);
        //if(fabs(df(x0))<0.00000000001)
        if(dfx0 == 0) {
            break;
        }
        double xi = x0 - f(x0) / df(x0);
        if(i+1 == vec[j]){
            printf("%.16f,\n ",xi);
            j++;
        }
        x0 = xi;
    }
}

void newton(double (*f)(double),double (*df)(double),double x0,int n ) {
    for(int i =0;i<n;i++) {
        double dfx0 = df(x0);
        //if(fabs(df(x0))<0.00000000001)
        if(dfx0 == 0) {
            break;
        }
        double xi = x0 - f(x0) / df(x0);
        printf("x_%d = %.16f \n",i+1,xi);
        x0 = xi;
    }
}

double df(double x) {
    return -6*x+2+3*pow(x,2);
    
}


double f(double x) {
    return pow(x,3)-3*pow(x,2)+2*x+0.42;
}

int main() {

    int vec[100] = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195};

    double x0 = 2.76622488;
    int n = 195;

    newton(f,df,x0,n);

    newtonvec(f,df,x0,n,vec);


    return 0;
}