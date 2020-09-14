#include <stdio.h>
#include <pwd.h>

int main(int argc, char **argv){
    struct passwd *u;

    while( (u = getpwent()) != NULL) {
	if (u->pw_uid >=1000)
	    printf("%s\n", u->pw_name);
	}

}
