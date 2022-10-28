#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <stdlib.h>
#include <string.h>

#define SERVER_PORT 5432
#define MAX_LINE 256

int main(int argc, char **argv) {
    FILE *fp;
    struct hostent *hp;
    struct sockaddr_in sin;
    char *host;
    char buf[MAX_LINE];
    int s;
    int len;

    if (argc != 2) {
        fprintf(stderr, "usage: tcp-client host\n");
        exit(1);
    }
    host = argv[1];

    /* translate host name into peer's IP address */

    hp = gethostbyname(host);
    if (!hp) {
        fprintf(stderr, "tcp-client: unknown host: %s\n", host);
       exit(1);
    }

    /* build address data structure */

    bzero((char *)&sin, sizeof(sin));
    sin.sin_family = AF_INET;
    bcopy(hp->h_addr, (char *)&sin.sin_addr, hp->h_length);
    sin.sin_port = htons(SERVER_PORT);

    /* active open */
    if ((s = socket(PF_INET, SOCK_STREAM, 0)) < 0) {
        perror("tcp-client: socket");
        exit(1);
    }

    if (connect(s, (struct sockaddr *)&sin, sizeof(sin)) < 0) {
        perror("tcp-client: connect");
        close(s);
        exit(1);
    }

    /* main loop: get and send lines of text */
    while (fgets(buf, sizeof(buf), stdin)) {
        buf[MAX_LINE - 1] = '\0';
        len = strlen(buf) + 1;
        send(s, buf, len, 0);
    }
return 0;
}
/*
Compilation 
$gcc tcp_client.c -o tcp_client
$./tcp_client <SERVER_IP>

*/
