#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int main(void) {
    unsigned int ui = UINT_MAX;
    signed char c = -1;

    if(c == ui) {
        printf("-1=4,294,967,295?\n");
    }
    return EXIT_SUCCESS;
}

