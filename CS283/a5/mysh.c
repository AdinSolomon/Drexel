// abs358@drexel.edu

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int DEBUG = 0;
enum {
	builtins_count = 1,
	bufsize = 512,
	maxargs = 256,
	maxbackground = 16
};
char *prompt;
const char *const builtins[builtins_count] = {"cd"};

void displayprompt();
char getinput(char *input);
int parse(char *input, char *argv[maxargs]);
int runcommand(char *argv[maxargs]);
int runcommand_background(char *argv[maxargs]);
int runcommand_builtin(char *argv[maxargs], int builtin);
void exitwith(int status);
char *rmnewline(char *str);

int
main(int argc, char *argv[])
{
	int status;
	char *input, *my_argv[maxargs];
	
	input = malloc(sizeof(char) * bufsize);
	
	status = 0;
	while (status == 0) 
	{
		prompt = "mysh: ";
		displayprompt();
		
		if (getinput(input) == '\0') { printf("\n"); break; } // no input with EOF
		
		parse(rmnewline(input), my_argv);
		runcommand(my_argv);
	}
	
	exitwith(status);
}

void
displayprompt()
{
	printf("%s", prompt);
}

char
getinput(char *input)
{
	memset(input, '\0', sizeof(char) * bufsize);
	fgets(input, sizeof(char) * bufsize, stdin);
	return *input;
}

int
parse(char *input, char *argv[maxargs])
{
	int i;
	
	i = -1;
	argv[++i] = strtok(input, " ");
	if (DEBUG > 0) { printf("testing: argv[%d] = %s\n", i, argv[i]); }
	while ((argv[++i] = strtok(NULL, " ")) != NULL && i < maxargs) {
		if (DEBUG > 0) { printf("testing: argv[%d] = %s\n", i, argv[i]); }
	}
	return i-1;
}

int
runcommand(char *argv[maxargs])
{
	int i, pid, status, background;
	const useconds_t patience = 10;
	
	if (DEBUG > 0) { printf("test: runcommand() start\n"); }

	// look for builtin commands
	if (DEBUG > 1) { printf("test: runcommand() builtin check\n"); }
	for (i = 0; argv[0] != NULL && i < builtins_count; i++) {
		if (strcmp(argv[0], builtins[i]) == 0) {
			return runcommand_builtin(argv, i);
		}
	}
	
	// check for backgrounding
	if (DEBUG > 1) { printf("test: runcommand() bg check\n"); }
	background = 0;
	i = -1;
	while (argv[++i] != NULL) { }
	if (argv[--i][strlen(argv[i]) - 1] == '&') {
		if (DEBUG > 2) { printf("test: runcommand() bg detected\n"); }
		background = 1;
		if (strlen(argv[i]) == 1) {
			if (DEBUG > 3) { printf("test: runcommand() bg & preceeded by space\n"); }
			argv[i] = NULL;
		}
		else {
			if (DEBUG > 3) { printf("test: runcommand() bg & with no space\n"); }
			argv[i][strlen(argv[i]) - 1] = '\0';
		}
		if (DEBUG > 2) { printf("test: runcommand() now without & argv[%d] = %s\n", i, argv[i]); }
	}
	if (DEBUG > 2) { printf("test: runcommand() int background = %d\n", background); }
	
	// do the thing
	pid = fork();
	if (pid < 0) {
		perror("fork");
		exit(1);
	}
	if (pid > 0) {
		if (DEBUG > 0) { printf("test: runcommand() parent\n"); }
		// check for backgrounding
		if (!(background)) {
			if (DEBUG > 2) { printf("test: runcommand() parent is waiting\n"); }
			wait(&status);
		} else {
			if ( DEBUG > 2) { printf("test: runcommand() parent is not waiting\n"); }
			usleep(patience); // to ensure that the child doesn't outspeed the parent's prompt
		}
	}
	else {
		if (DEBUG > 0) { printf("test: runcommand() child\n"); }
		execvp(argv[0], argv);
		perror("execvp");
		exit(2);
	}
}

int
runcommand_background(char *argv[maxargs])
{
	
}

int
runcommand_builtin(char *argv[maxargs], int builtin)
{
	switch (builtin) {
		case 0: // cd
			if (argv[1] == NULL) {
				chdir("~");
			} else
			if (chdir(argv[1]) != 0) {
				printf("cd failed - directory has not been changed\n");
			}
			break;
		
		default: // something has gone horribly wrong
		perror("you done goofed - check your builtins declaration");
		exit(2);
	}
	return 0;
}

void
exitwith(int status)
{
	exit(status);
}

char *
rmnewline(char *str)
{
	int i = -1;
	while(i < bufsize && str[++i] != '\n') {}   
	str[i] = '\0';
	return str;
} 
