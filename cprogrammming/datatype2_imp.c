#include<stdio.h>
#include<stdlib.h>
#include<limits.h>
#include<stddef.h>

char *copy(size_t n, const char *str){
char *p;
size_t i;
if(n==0){
	return NULL;
}
p = (char *)malloc(n);
if(p==NULL){
	return NULL;
}
for(i=0;i<n;i++){
	p[i] = *str++;
}
return p;
}

int main(int argc, char **argv){

size_t tainted_int = UINT_MAX / 2 + 100;
char *p;
char *str = (char *)calloc(1, tainted_int);
if(str == NULL){
return EXIT_FAILURE;
}
strcpy(str, "Hello, World!");
p = copy(tainted_int, str);
if(p==NULL){
return EXIT_FAILURE;
}
}

