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


double f(double d) {
    //return 1761463*exp(x)+(201256/x)*(exp(x)-1)-3665017;
    //return 1425622*exp(x)+(109079/x)*(exp(x)-1)-2614229;  //Q27
    //return ((9.81*x)/16.16)*(1-exp(-(16.16/x)*8.05))-35.0;
    //return ((9.81*63.24)/x)*(1-exp(-(x/63.24)*9.36))-41.29;
    //return sqrt(2*9.81*x)*tanh((sqrt(2*9.81*x)/(2*5.48))*9.4)-9.04; //agua no cano
    //return 1-(((pow(71.89,2))/(9.81*pow(1.58*x+(pow(x,2)/2),3)))*(1.58+x));
    //return 2*asin(1.0)*pow(x,2)*((3*6.08-x)/3.0)-447.51;
    //return ((4/3.0)*2*asin(1.0)*pow(5.78,3))*(433.18+1000)+1000*((2*asin(1.0)*pow(x,2)*(3*5.78-x))/3.0);
    //return 1000.0*((6243584.0*2*asin(1.0))/46875.0-(2*asin(1.0)*(348/25.0-x)*pow(x,2))/3.0)-(22693866944.0*2*asin(1.0))/1171875.0;
    //return (((2*asin(1.0)*8.59)/3.0)*(pow(2.0,2)+pow(7.73,2)+2.0*7.73))*599.17-1000.0*((2*asin(1.0)*(8.59-x))/3.0)*(pow(2.0,2)+pow(7.73,2)+2.0*7.73);
    double a = 67100; //k1
    double b = 61; //k2
    double m = 147;
    double g = 9.81;
    double h = 0.72;

    return 2.0*b*pow(d,5/2.0)/5.0 + 1.0*a*pow(d,2)/2.0 - m*g*d - m*g*h;
}

double df(double d) {
    double a = 67100; //k1
    double b = 61; //k2
    double m = 147;
    double g = 9.81;
    double h = 0.72;
    return b*pow(d,3/2.0)+a*d-g*m;
    
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

    int vec[100]={1 , 4, 7, 10};
    double a = 0.0;
    double b = 1.29;
    int n = 10;
    double tol = 0.0000000000001;
    printf("\nBISSECAO EM VETOR: \n");
    bissectionvec(f,a,b,n,tol,vec);


    //Newton:

    int vecn[100] = {1,3,6};

    double x0n = 1.1;
    int nn = 6;

    printf("\nNEWTON EM VETOR: \n");
    newtonvec(f,df,x0n,nn,vecn);


    //Secante:
    //double x0 = 0.1;
    //double x1 = 1.62;
    
    double x0 = 0.94;
    double x1 = 2.1;
    int ns = 8;
    int vecs[100]={1,2,5,8};
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
    double af = 0.0;
    double bf = 1.55;
    int nf = 11;
    int vec2[100] = {2,5,7,11};
    printf("\nPOSICAO FALSA em vetor: \n");
    PosicaoFalsaVECT(f,af,bf,nf,vec2);

    return 0;
}