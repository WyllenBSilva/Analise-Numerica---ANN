#include <stdio.h>
#include <math.h>

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


void PosicaoFalsaVECT(double (*f)(double),double a,double b,int n, int vec[]) {

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

void secante(double (*f)(double),double x0,double x1,int n, int vec[]) {

    int j = 0;

    for(int i = -1;i<n;i++) {
        double fx0 = f(x0);
        double fx1 = f(x1);
        if(fx0 == fx1) {
            break;
        }
        double x2 = (x0*fx1-x1*fx0) / (fx1-fx0);
        if(i+2 == vec[j]) {
            printf("%.16f,\n",x2);
            j++;
        }

        x0 = x1;
        x1 = x2;
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


double f(double w) {
    //usando x como parametro por que fica melhor de calcular a derivada pelo site.

    double g = 9.81;
    double x = 1.15;
    double t = 0.86;

    return (-g / (2 * pow(w,2))) * (sinh(w * t) - sin(w * t)) - x;
}

double df(double w) {

    double g = 9.81;
    double x = 1.15;
    double t = 0.86;

    //return -g*x*sinh(t*x)-(g*t*pow(x,2)*cosh(t*x))/2.0-t*cos(t*x);
    return (g * (t * w * cos(t * w) - t * w * cosh(t * w) - 2.0 * sin(t * w) + 2.0 * sinh(t * w)))/(2.0 * pow(w, 3));
    
}


//newton:


void newtonvec(double(*f)(double),double(*df)(double),double x0,int n, int vec[]) {
    int j = 0;
    for(int i =0;i<n;i++) {
        
        double dfx0 = df(x0);
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

//Para o método do ponto fixo:
double g(double x) {
    //return 
}

int main() {


    //Bisseção:

    //int vec[100] = {2, 4, 8, 12};
    //double a = 0.1;
    //double b = 1.25;

    //int vec[100] = {2 , 4, 8, 12};
    //double a = 0.1;
    //double b = 1.78;

    //−5.46,0.4

    int vec[100]={2 , 4, 8, 12};
    double a = -5.46;
    double b = 0.92;
    int n = 12;
    double tol = 0.0000000000001;
    printf("\nBISSECAO EM VETOR: \n");
    bissectionvec(f,a,b,n,tol,vec);


    //Newton:

    

    double x0n = -1.27;
    int vecn[100] = {1,3,5};
    int nn = 5;

    printf("\nNEWTON EM VETOR: \n");
    newtonvec(f,df,x0n,nn,vecn);


    //Secante:
    double x0 = -4.23;
    double x1 = -1.9;
    int ns = 5;
    int vecs[100]={1,2,5};
    //1 2 e 5 interacoes
    printf("\n\nMETODO DA SECANTE em vetor: \n");
    secante(f,x0,x1,ns,vecs);



    //Ponto Fixo: (nao foi utilizado nessa questao)
    //int n = 8;
    //double x0 = 1.67175;
    //int vec[100] = {1, 2, 3, 4, 5, 6, 7, 8};
    //fixed_pointVECT(g,x0,n,vec);
    


    //Posição Falsa:
    //double af = 0.1;
    //double bf = 1.76;
    double af = -5.15;
    double bf = 0.77;
    int nf = 11;
    int vec2[100] = {2,4,7,11};
    printf("\nPOSICAO FALSA em vetor: \n");
    PosicaoFalsaVECT(f,af,bf,nf,vec2);

    return 0;
}