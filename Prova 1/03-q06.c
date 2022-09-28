#include <stdio.h>
#include <math.h>
#define L 4
#define C 4

void jacobi(double A[L][C], double B[L], double chute[L], int n){
    for(int k=0;k<n;k++){
        for(int i=0;i<L;i++){
            double bi=B[i];
            for(int j=0;j<C;j++){
                if(j!=i) bi-=A[i][j]*chute[j];
            }
            bi/=A[i][i];
            printf("x_%d(%d) = %.16f | ", i+1, k+1, bi);
            chute[i]=bi;
        }
        printf("\n");
    }
}


// INSERIR O TAMANHO DA MATRIZ EM DEFINE
//***************************************************************************

int main(){
    double A[L][C]={{-10.73, -2.9, 4.36, -1.89}, {3.3, 6.28, 0.69, 0.71}, {-3.36, -1.9, 7.05, -0.2}, {0.85, -0.08, 0.83, 3.35}};
    double B[L]={-4.62, 3.56, 4.25, -3.82}; // result

    double chute[L]= {-2.08, 2.26, 2.46, -0.55}; //x0
    int n=29;

    jacobi(A, B, chute, n);

    return 0;
}