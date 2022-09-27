#include <stdio.h>

#define numRows 4
#define numCols 3

//so funciona para sistemas nxn 

void print_matrix(double m[numRows][numCols]) {
    for(int i =0;i<numRows;i++) {
        for(int j =0;j<numCols;j++) {
            printf("%.8f,\t ",m[i][j]);
        }
        printf("\n");
    }
}

void gauss(double E[numRows][numCols]) {
    for(int j=0; j < numCols-1;j++) {
        for(int i = j;i<numRows;i++) {
            if(E[i][j] != 0) {
                if(i!=j) {
                    //troca as linhas i e j
                    
                    for(int k=0;k<numCols;k++) {
                        double temp = E[i][k];
                        E[i][k] = E[j][k];
                        E[j][k] = temp;
                    }

                }
                //zerar todos os elementos da coluna j
                //abaixo do elemento na posicao j,j
                for(int k = j+1; k< numRows;k++) {
                    double m = -E[k][j] / E[j][j]; //pivô
                    for(int p = j; p<numCols;p++) {
                        E[k][p] = m*E[j][p] + E[k][p];
                    }
                }
                printf("\n");
                print_matrix(E);
                
                break;
            }
        }
    }

    printf("\n");
    for(int i = 0;i<numRows;i++) {
        double xi = E[i][numCols-1]/E[i][i];
        printf("X_%d = %.16f\n",i+1, xi );
    }
}


int main() {

    double k = 7/5.0;
    double n = -2.0;
    double w = -9/2.0;
    double g = 1/9.0;

    

    double E[numRows][numCols] = {
        {1.0, -2.6666666666666665, -0.2},
        {-0.53333334,     -1.23333333,    -1.57333333},
        {3.26666667,      0.20000000,     1.12000000},
        {g*-4.27777778,     g*12.80000000,    g*1.47142857}
        
        
    };


    print_matrix(E);
    
    //gauss(E);
    //solucao exata é 2,1,-1,1
    //ver se a questao pede a solucao exata

    //matrixcalc, usar ele

    //rever esse código pq está diferente do professor

    return 0;
}