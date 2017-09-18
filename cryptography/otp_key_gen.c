#include <stdio.h>
#define LEN 12

int main(int argc, char **argv){
    FILE *randfile, *outputfile;

    int c;
    unsigned char next;

    randfile = fopen("/dev/random","r");
    outputfile = fopen("otp_key.txt", "w");

    if( (randfile == NULL) || (outputfile == NULL)) {
        printf("File Errors:\n");
        return 0;
    }

    for(c = 0; c < LEN; c++){
        fscanf(randfile, "%c", &next);
        fprintf(outputfile, "%02X", next);
    }

    fclose(randfile);
    fclose(outputfile);

    return 0;

}
