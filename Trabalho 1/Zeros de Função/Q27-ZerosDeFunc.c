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



double f(double x) {
    double P = 1784116; //Po
    double v = 428465;
    double I = 4058169; //P (individuos)
    return P*exp(x)+(v/x)*(exp(x)-1)-I;  //Q27
}

double df(double x) {
    double P = 1784116; //Po
    double v = 428465;
    double I = 4058169; //P (individuos)

    return ((P*pow(x,2)+v*x-v)*exp(x)+v)/pow(x,2);
    
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


int main() {


    //Bisseção:
    int vec[100]={2 , 4, 8, 12};
    double a = 0.1; 
    double b = 1.27;
    int n = 12;
    double tol = 0.0000000000001;
    printf("\nBISSECAO EM VETOR: \n");
    bissectionvec(f,a,b,n,tol,vec);


    //Newton:
    int vecn[100] = {1,3,5};
    double x0n = 1.81;
    int nn = 5;
    printf("\nNEWTON EM VETOR: \n");
    newtonvec(f,df,x0n,nn,vecn);


    //Secante:

    double x0 = 0.1;
    double x1 = 1.39;
    int ns = 5;
    int vecs[100]={1,2,5};
    //1 2 e 5 interacoes
    printf("\n\nMETODO DA SECANTE em vetor: \n");
    secante(f,x0,x1,ns,vecs);    

    //Posição Falsa:
    double af = 0.1;
    double bf = 1.6;
    int nf = 11;
    int vec2[100] = {2,4,7,11};
    printf("\nPOSICAO FALSA em vetor: \n");
    PosicaoFalsaVECT(f,af,bf,nf,vec2);

    return 0;
}