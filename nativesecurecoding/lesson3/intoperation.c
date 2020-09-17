#include <stdio.h>
#include <stdlib.h>


int f(void);
void g(void);
void h(void);
void i(void);

int main(void) {
    char c;

   if ((c=f())==-1) {
       //The int value returned by the function is truncated when stored as char and then converted back to int 
       //width before the comparison. 
       //
       printf("c=%d.\n",c);
    }

    //assignment 
    g();

    //misinterpreted values
    h();

    //truncation 
    i();

    return EXIT_SUCCESS;
}

int f(void) {
    return 255;
    }

void g(void) {
    char c;
    int i = 255;
    long l;

    l = (c=i);
    printf("l=%ld.\n",l);
    return;
}

void h(void) {
    int si = -3;

    //Because the new type is unsigned, the value is converted by repeatedly adding or subtracting one more than the maximum 
    //value that can be represented in the new type, until tje value is in the range of the new type. 
    unsigned int ui = si;

    //If accessed as an unsigned value, the resulting value will be misinterprested as a large, positive value
    //
    printf("ui=%u\n", ui);
    return;
}

void i(void) {
    unsigned char sum;

    unsigned char c1 = 200;
    unsigned char c2 = 90;
    sum = c1 + c2;
    printf("sum=%u\n",sum);

    return;
}

