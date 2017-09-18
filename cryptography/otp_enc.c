#include <stdio.h>
#define LEN 12

int main(int argc, char **argv){
    FILE *keyfile, *plainfile, *cipherfile;

    int c;

    unsigned char temp;
    char temp1;


    keyfile = fopen("otp_key.txt", "r");
    plainfile = fopen("plain.txt", "r");
    cipherfile = fopen("cipher.txt", "w");


    if( (keyfile == NULL) || (plainfile == NULL) || (cipherfile == NULL)){
        printf("File Opening Error!!!\n");
        return -1;
    }

    for(c = 0; c < LEN; c++){
        fscanf(keyfile, "%2hhX", &temp);
        fscanf(plainfile, "%c", &temp1);
        fprintf(cipherfile, "%02X", temp ^ temp1);
    }

    fclose(keyfile);
    fclose(plainfile);
    fclose(cipherfile);

return 0;
}
