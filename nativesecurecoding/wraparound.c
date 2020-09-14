#include<stdio.h>
#include<limits.h>
#include<stdlib.h>

int main(int argc, char **argv){
unsigned int ui;

ui = UINT_MAX;
printf("\nui=%u",ui);
printf("\nWe are going to add 1 to ui:");
ui++;
printf("\nui=%u\n",ui);

return EXIT_SUCCESS;

}
