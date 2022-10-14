#include <stdio.h>

#define L 3
#define C 3


//so funciona para sistemas nxn

void jacobi(double A[L][C], double B[L], double chute[L], int n){
    double next[L];
    for(int k=0;k<n;k++){
        for(int i=0;i<L;i++){
            double bi=B[i];
            for(int j=0;j<C;j++){
                if(j!=i) bi-=A[i][j]*chute[j];
            }
            bi/=A[i][i];
            printf("x_%d(%d) = %.16f | ", i+1, k+1, bi);
            next[i]=bi;
        }
        printf("\n");
        //atualizar o chute
        for(int i=0;i<L;i++) chute[i]=next[i];
    }
}

int main(){
    double A[L][C]={{5.91, -2.26, -2.44}, {0.06, -1.31, 0.04}, {-1.06, -2.09, -4.35}};

    double B[L]={0.22, 1.73, 4.08}; // result

    double chute[L]={0.97, 1.49, 4.0}; // x0
    int n=19;
    
    jacobi(A, B, chute, n);

    //int vec[100] = {1, 5, 6, 7, 10, 12, 17, 19};
    //jacobivec(A,B,chute,n,vec);

    return 0;
}