#include <stdio.h>
#define LEN 12

int main(int argc, char **argv){
    FILE *keyfile, *plainfile, *cipherfile;

    int c;

    unsigned char temp;
    char temp1;


    keyfile = fopen("otp_key.txt", "r");
    plainfile = fopen("plain2.txt", "w");
    cipherfile = fopen("cipher.txt", "r");


    if( (keyfile == NULL) || (plainfile == NULL) || (cipherfile == NULL)){
        printf("File Opening Error!!!\n");
        return -1;
    }

    for(c = 0; c < LEN; c++){
        fscanf(keyfile, "%2hhX", &temp);
        fscanf(cipherfile, "%2hhX", &temp1);
        fprintf(plainfile, "%c", temp ^ temp1);
    }

    fclose(keyfile);
    fclose(plainfile);
    fclose(cipherfile);

return 0;
}
