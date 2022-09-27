#include <stdio.h>



int main() {

    //só altero isso:
    //int k1=423, k2=446, k3=762, k4=748, k5=453, k6=410, k7=317  , k8=351;
    //int k1=526, k2=587, k3=472, k4=375, k5=453, k6=410, k7=384,  k8=463;

    int k1=202, k2=240, k3=537, k4=527, k5=794, k6=694, k7=409,  k8=481;
    int x2 = k6 - k5; //x3 + k6 = k5 + x2
    int x4 = k7 - k8;   //X4 + k8 = k7 + x3
    int x1 = k1 - k2 + x4; //x1 + k2 = k1 + x4

    //converte pra positivo e soma
    x2 *= -1;
    x2++;

    x4 *= -1;
    x4++;
    
    x1 *= -1;
    x1++;

    printf("x1 = %d\n",x2);
    printf("x2 = %d\n",x4);
    printf("x3 = %d\n",x1);

    return 0;
}