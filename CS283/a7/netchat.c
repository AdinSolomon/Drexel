// abs358@drexel.edu

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <netdb.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

enum {
    Nbuf = 1024
};
int sock;

void *horton(void *NEVERUSED);

int
main(int argc, char *argv[])
{
    struct sockaddr_in listener;
    struct hostent *host;
    pthread_t tid;
    char buf[Nbuf], *temp;
    int n;

    // we need a username - no other args will be considered
    if (argc == 1) {
        printf("Usage: ./netchat username\n");
        exit(1);
    }

    // set up the connection
    sock = socket(AF_INET, SOCK_STREAM, 0);
    host = gethostbyname("tux2.cs.drexel.edu");
    listener.sin_family = AF_INET;
    listener.sin_port = htons(2020);
    listener.sin_addr.s_addr = *((long *) host->h_addr_list[0]);
    if (connect(sock, (struct sockaddr *) &listener, sizeof(struct sockaddr_in)) != 0) {
        perror("connect");
        exit(2);
    } else { printf("connection was successful\n"); }

    // send over the username from the commandline
    if (send(sock, argv[1], strlen(argv[1]), 0) == -1) {
        perror("send");
        exit(3);
    }

    // start listening 
    if (pthread_create(&tid, NULL, horton, NULL) != 0) {
        perror("pthread_create");
        exit(1);
    }
    
    // start sending messages
    while (fgets(buf, sizeof(char)*Nbuf, stdin) != NULL) {
        if ((n = strlen(buf)) != Nbuf && strchr(buf, '\n') == NULL) { // fix input without newline (includes empty input)
            buf[n] = '\n';
            buf[++n] = '\0';
        }
        if (send(sock, buf, n, 0) < 0) {
            perror("send");
            exit(1);
        }
    }
    printf("\n");

    // no need to stop the other thread, just exit
    exit(0);
}

void *
horton(void *NEVERUSED)
{
    ssize_t n;
    char who[Nbuf];

    while (1) {
        if ((n = recv(sock, who, Nbuf, 0)) == -1) {
            perror("recv");
            exit(4);
        }
        who[n] = '\0';
        printf("%s", who);
    }
}