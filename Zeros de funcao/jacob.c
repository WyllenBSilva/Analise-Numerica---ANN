#include <stdio.h>

#define numRows 3
#define numCols 4


//so funciona para sistemas nxn
void jacobi(double E[numRows][numCols],double chute[numRows],int n ) {
    for(int i =0 ; i<n; i++) {
        double resp[numRows] = {};
        for(int j =0;j<numRows;j++) {
            double bj = E[j][numCols-1];
            double soma = 0;
            for(int k=0;k<numCols-1;k++) {
                if(k!=j) {
                    soma -= E[j][k] * chute[k];
                }
            }
            double xj = (bj + soma ) / E[j][j];
            resp[j] = xj;
            printf("X_%d^(%d) = %.10f\t",j+1,i+1,xj);
        }
        printf("\n");
        for(int i = 0;i<numRows;i++) {
            chute[i]=resp[i];
        }
    }
}



int main() {

    double E[numRows][numCols] = {
        {4,2,-1,11},
        {1,-5,1,-4},
        {1,1,-6,9}
    };

    double chute[numRows] = {0,0,0};
    int n = 10;

    jacobi(E,chute,n);

    

    return 0;
}