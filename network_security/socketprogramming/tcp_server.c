#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <stdlib.h>
#include <string.h>

#define SERVER_PORT 5432
#define MAX_PENDING 5
#define MAX_LINE 256

int make_upper(char *userdata) {
    char *temp = userdata;
    while (*temp) {
        *temp = toupper((unsigned char) *temp);
        temp++;
    }
    return 0;
}


int main() {
    struct sockaddr_in sin;
    char buf[MAX_LINE];
    int len;
    int s, new_s;

    /* build address data structure */
    bzero((char *)&sin, sizeof(sin));
    sin.sin_family = AF_INET;
    sin.sin_addr.s_addr = INADDR_ANY;
    sin.sin_port = htons(SERVER_PORT);

    /* setup passive open */
    if ((s = socket(PF_INET, SOCK_STREAM, 0)) < 0) {
        perror("tcp-server: socket");
        exit(1);
    }

    if ((bind(s, (struct sockaddr *)&sin, sizeof(sin))) < 0) {
        perror("tcp-server: bind");
        exit(1);
    }

    listen(s, MAX_PENDING);
    /* wait for connection, then receive and print text */

    while(1) {
        if ((new_s = accept(s, (struct sockaddr *)&sin, &len)) < 0) {
            perror("tcp-server: accept");
            exit(1);
        }
        while (len = recv(new_s, buf, sizeof(buf), 0)) {
                make_upper(buf);
                //char *data = make_upper(buf);
                /*while (*data) {
                *data = toupper((unsigned char) *data);
                data++;
                } */

            fputs(buf, stdout);
            }
        close(new_s);
    }

return 0;
}

/* 
Compilation
$gcc tcp_server.c -o server
$./server 

You should see the tcp server is running on port 5432. 

$netstat -antp 

*/
