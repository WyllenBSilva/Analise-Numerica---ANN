#include <stdio.h>
#include <math.h>

#define ROW 4
#define COL 4

#define L1 0
#define L2 1
#define L3 2
#define L4 3


void imprimeMatriz(double matriz[ROW][COL]){
    for(int row = 0; row < ROW; row++){
        for(int col = 0; col < COL; col++){
            printf("%.16f, ", matriz[row][col]);
        }
        printf("\n");
    }
}

void trocaLinha(double matriz[ROW][COL], int r1, int r2){
        for(int k=0;k<COL;k++){
        double temp = matriz[r1][k];
        matriz[r1][k] = matriz[r2][k];
        matriz[r2][k] = temp;
    }
}

void operacaoEmLinha(double matriz[ROW][COL], int row, double num){
    for(int i = 0; i < COL; i++){
        matriz[row][i] *= num; 
    }
}

void opercaoEmDuasLinhas(double matriz[ROW][COL], int target, int r2, double num){
    for(int i = 0; i < COL; i++){
        matriz[target][i] = (num*matriz[r2][i]) + matriz[target][i];
    }
}

void operacoes(double matriz[ROW][COL]){
    /*
	L1 0
    L2 1
    L3 2
	L4 3
	***quem soma vem primeiro
	
	//1/6⋅L3+L4→L4
	opercaoEmDuasLinhas(matriz, 3, 2, (1.0/6.0) );
	//L1↔L2
	trocaLinha(matriz, 0, 1);
	//8/3⋅L2→L2
	operacaoEmLinha(matriz, 1, (8.0/3.0));
	//L1↔L4
	trocaLinha(matriz, 0, 3);
	//−3/4⋅L1→L1
	operacaoEmLinha(matriz, 0, (-3.0/4.0));
	//4/5⋅L2+L1→L1
	opercaoEmDuasLinhas(matriz, 0, 1, (4.0/5.0));*/

    /*
    −8/3⋅L1+L2→L2 ,
    −2⋅L1+L3→L3,
    −2⋅L1+L4→L4,
    −6/29⋅L2+L3→L3,
    −9/29⋅L2+L4→L4
            −357/557⋅L3+L4→L4
    */

	//−8/3⋅L1+L2→L2 ,
	opercaoEmDuasLinhas(matriz, L2,L1,(-8.0/3.0));
	//−2⋅L1+L3→L3,
	opercaoEmDuasLinhas(matriz, L3, L1, (-2.0));
	//−2⋅L1+L4→L4,
	opercaoEmDuasLinhas(matriz, L4, L1, (-2.0));
    //−6/29⋅L2+L3→L3,
    opercaoEmDuasLinhas(matriz, L3, L2, (-6.0/29.0));
    //−9/29⋅L2+L4→L4
    opercaoEmDuasLinhas(matriz, L4, L2, (-9.0/29.0));
    //−357/557⋅L3+L4→L4
    opercaoEmDuasLinhas(matriz, L4, L3, (-357.0/557.0));

    imprimeMatriz(matriz);
}

int main(){
    double matriz[ROW][COL] = {
		{-3, 5, -8, -6},
        {-8, -6, -3, -6},
        { -6, 6, 7, 7},
        {-6, 4, 2, -4}
    };

    printf("Matriz Original:\n");
    imprimeMatriz(matriz);
    printf("Resultado:\n");
    operacoes(matriz);
    return 0;
}