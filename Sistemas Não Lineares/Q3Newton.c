#include <stdio.h> 

double f1(double x, double y) {
    //func1 = x**2 + y**2 - 5
    return pow(x,2) + pow(y,2) - 5;
}

double f2(double x, double y) {
    //func2 = x**2 + x * y**3 - 3
    return pow(x,2) + x * pow(y,3) - 3;
}

double f1x(double x, double y) { //derivada de f1 em relacao a x
    return 2*x;
}

double f1y(double x, double y) { //derivada de f1 em relacao a y
    return 2*y;
}

double f2x(double x, double y) { //derivada de f2 em relacao a x
    return 2*x+pow(y,3);
}

double f2y(double x, double y) { //derivada de f2 em relacao a y
    return 3*x*pow(y,2);
}

void newtonSistemaslineares(double x0, double y0, int n) {

    for(int i = 0;i<n;i++) {

        double a = f1x(x0,y0);
        double b = f1y(x0,y0);
        double c = f2x(x0,y0);
        double d = f2y(x0,y0);
        double det = a * d - b * c;

        double xk = x0 - (f2y(x0,y0) * f1(x0,y0) - f1y(x0,y0) * f2(x0,y0)) / det; 
        double yk = y0 - (-f2x(x0,y0) * f1(x0,y0) + f1x(x0,y0) * f2(x0,y0)) / det;
    
        x0 = xk;
        y0 = yk;
        
        printf("x^(%d) = %.16f \t y^(%d) = %.16f,\n", i + 1, x0, i+1, y0 );

    }

}

int main() {

    int n = 5;

    double x0 = -2.3213;
    double y0 = 1.3224;

    newtonSistemaslineares(x0,y0,n);


    return 0;
}