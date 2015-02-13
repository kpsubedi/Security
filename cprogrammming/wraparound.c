#include<stdio.h>
#include<limits.h>
#include<stdlib.h>

int main(int argc, char **argv){
unsigned int ui;

ui = UINT_MAX;
ui++;
printf("\nui=%u",ui);

return EXIT_SUCCESS;

}
