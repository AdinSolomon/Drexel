// abs358@drexel.edu

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

enum nums {
	options_count = 8,
	argc = 8,
	arg_buf = 256
};
const char * const options[options_count] = {"./ccadd", "./ccitem", "./cclist", "./ccdel", "./ccmatch", "./ccyear", "./ccedit", "quit"};
char *argv[argc];

void prompt();
char *rmnewline(char *str);
void runcommand(int nargs);

int
main()
{
	int option, nargs;
	
	for (int i = 0; i < argc; i++) {
		if ((argv[i] = malloc(sizeof(char) * arg_buf)) == NULL) {
			perror("malloc");
			exit(1);
		}
	}
	
	while (1) {
		prompt();
		
		// read the user's menu choice
		argv[0][0] = '\0';
		fgets(argv[0], sizeof(char) * arg_buf, stdin);
		if (*(argv[0]) == '\0') { exit(0); }
		option = atoi(rmnewline(argv[0]));
		
		// process user request
		if (option == 1) {
			printf("You chose %s\n", options[0]);
			strcpy(argv[1], "id");
			strcpy(argv[2], "maker");
			strcpy(argv[3], "model");
			strcpy(argv[4], "year");
			strcpy(argv[5], "cpu");
			strcpy(argv[6], "description");
			nargs = 6;
		} else
		if (option == 2) {
			printf("You chose %s\n", options[1]);
			strcpy(argv[1], "id");
			nargs = 1;
		} else
		if (option == 3) {
			printf("You chose %s\n", options[2]);
			nargs = 0;
		} else
		if (option == 4) {
			printf("You chose %s\n", options[3]);
			strcpy(argv[1], "id");
			nargs = 1;
		} else
		if (option == 5) {
			printf("You chose %s\n", options[4]);
			strcpy(argv[1], "string");
			nargs = 1;
		} else
		if (option == 6) {
			printf("You chose %s\n", options[5]);
			strcpy(argv[1], "start");
			strcpy(argv[2], "end");
			nargs = 2;
		} else
		if (option == 7) {
			printf("You chose %s\n", options[6]);
			strcpy(argv[1], "id");
			nargs = 1;
		} else
		if (option == 8) {
			break;
		} else {
			continue;
		}
		
		strcpy(argv[0], options[option - 1]);
		runcommand(nargs);
	}
	exit(0);
}

void
prompt()
{
	int i;
	printf("Please choose one of the following options:\n");
	for (i = 0; i < options_count; i++) {
		printf("\t%d. %s\n", i+1, options[i]);
	}
	printf("Enter a number:\n");
}

char *
rmnewline(char *str)
{
	int i = -1;
	while(str[++i] != '\n') {}
	str[i] = '\0';
	return str;
}

void
runcommand(int nargs)
{
	int i, pid, status;
	char *temp;
	
	temp = malloc(sizeof(char) * arg_buf);
	for (i = 1; i <= nargs; i++) {
		printf("Please enter a(n) %s: ", argv[i]);
		while (1) {
			temp[0] = '\0';
			fgets(temp, sizeof(char) * arg_buf, stdin);
			if (*temp == '\0') { exit(0); }
			if (temp[0] != '\n') { break; }
			printf("Please enter a(n) %s of legth>0: ", argv[i]);
		}
		printf("\tyou entered: \"%s\"\n", strcpy(argv[i], rmnewline(temp)));
	}
	temp = argv[i];
	argv[i] = NULL;
	
	pid = fork();
	if (pid < 0) {
		perror("fork");
		exit(2);
	}
	if (pid > 0) {
		// this is the parent, so wait for child
		wait(&status);
		argv[i] = temp;
	}
	else {
		// this is the child, so execvp
		execvp(argv[0], argv);
		perror("exec");
		exit(3);
	}
}
