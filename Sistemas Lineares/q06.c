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
    double A[L][C]={{7.02, -3.91, -0.19, 1.11}, {-0.35, 5.38, 1.82, 1.4}, {-1.98, 4.62, -9.87, 1.45}, {2.11, 0.91, -3.31, -8.13}};
    double B[L]={-2.68, -0.0, 2.36, -2.85}; // result

    double chute[L]= {-4.02, -2.85, 3.01, 2.82}; //x0
    int n=25;

    jacobi(A, B, chute, n);

    return 0;
}