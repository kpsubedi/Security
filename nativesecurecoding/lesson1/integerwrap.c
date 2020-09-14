#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

unsigned int unsigned_int_sum(unsigned int i, unsigned int j);
unsigned int unsigned_int_difference(unsigned int i, unsigned int j);

int main(void) {
    unsigned int ui;
    
    ui = UINT_MAX; //4,294,967,295 on x86-32;
    
    ui++;
    printf("ui = %u\n", ui);
    
    ui = 0;
    ui--;

    printf("ui = %u\n", ui);

    //Avoid wraparound errors when checking against maximum values 

    printf("sum = %u\n", unsigned_int_sum(UINT_MAX, 1));

    //Avoid wraparound erros when checking against the minimum unsigned value 0
    //

    printf("difference = %u\n", unsigned_int_difference(0,1));

    return EXIT_SUCCESS;
}

#if 0
//unsigned addition (broken)
//
unsigned int unsigned_int_sum(unsigned int i, unsigned int j) {
    if( i + j > UINT_MAX) { //cannot happen
        puts("wrap around occured");
        //saturation semantics
        return UINT_MAX;
    } else 
        return i + j;
    }
#endif 

#if 1 
//unsigned addition (corrected)
//
unsigned int unsigned_int_sum(unsigned int i, unsigned int j) {
    //test eliminates the possibility of wraparound 
    //
    if ( i > UINT_MAX - j) {
        puts("wrap around occured");
        return UINT_MAX; //saturation semantics 
    } else 
        return i + j;
}
#endif 

#if 0 
//unsigned subtraction (broken)

unsigned int unsigned_int_difference(unsigned int i, unsigned int j) {
    if ( i - j < 0) { //cannot happen 
        puts("wrap around occured");
        return 0;
    } else 
        return i + j;
}
#endif 

#if 1 
//unsigned subtraction (corrected)

unsigned int unsigned_int_difference(unsigned int i, unsigned int j) {
    //test eliminates the possibility of wraparound 
    if ( i < j) {
        puts("wrap around occured");
        return 0;
    } else 
        return i - j;
}
#endif
