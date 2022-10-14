#include <stdio.h> 

double f1(double x, double y) {
        return x * x + y * y - 5;
}

double f2(double x, double y) {
    return x * x - y * y - 3;
}

double f1x(double x, double y) {
    return 2 * x;
}

double f1y(double x, double y) {
        return 2*y;
}

double f2x(double x, double y) {
    return 2*x;
}

double f2y(double x, double y) {
    return -2*y;
}

int main() {

    int n = 5;

    double x0 = 3;
    double y0 = 5;

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
        printf("x^(%d) - %.12f \t y^(%d) = %.12f\n", i + 1, x0, i+1, y0 );

        //matriz jacobiana:

        //
    }

    //exemplo:
    


    return 0;
}