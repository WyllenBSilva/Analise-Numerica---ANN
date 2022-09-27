#include <stdio.h>

#define numRows 3
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

void Matriz_Formatada(double m[numRows][numCols]) {
    for(int i =0;i<numRows;i++) {
        printf("{");
        for(int j =0;j<numCols;j++) {
            
            if(i==j) {
                printf("%.8f\t ",m[i][j]);
            } else {
printf("%.8f,\t ",m[i][j]);
            }
        }
        printf("},\n");
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
    double l = -9/2.0;
    double h = 1/9;
    

    double E[numRows][numCols] = {
        {k*2.3333333333333335, k*0.14285714285714285, k*0.8},
        {6.0, -0.8333333333333334, 0.6666666666666666},
        {0.2222222222222222, 0.8, 0.5714285714285714},
        {1.0, -2.6666666666666665, -0.2}
        
    };


    print_matrix(E);
    
    //gauss(E);
    //solucao exata é 2,1,-1,1
    //ver se a questao pede a solucao exata

    //matrixcalc, usar ele

    //rever esse código pq está diferente do professor

    return 0;
}