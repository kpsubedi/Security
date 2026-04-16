#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>

#define ALLOWED_IP "127.3.3.1"

int main() {
    char ip_addr[128];
    struct in_addr to_ping_host, trusted_host;

    // get address
    if (!fgets(ip_addr, sizeof(ip_addr), stdin))
        return 1;
    ip_addr[strcspn(ip_addr, "\n")] = 0;

    // verify address
    if (!inet_aton(ip_addr, &to_ping_host))
        return 1;
    char *ip_addr_resolved = inet_ntoa(to_ping_host);

    // prevent SSRF
    if ((ntohl(to_ping_host.s_addr) >> 24) == 127)
        return 1;

    // only allowed
    if (!inet_aton(ALLOWED_IP, &trusted_host))
        return 1;
    char *trusted_resolved = inet_ntoa(trusted_host);

    if (strcmp(ip_addr_resolved, trusted_resolved) != 0)
        return 1;

    // ping
    char cmd[256];
    snprintf(cmd, sizeof(cmd), "ping '%s'", ip_addr);
    system(cmd);
    return 0;
}
