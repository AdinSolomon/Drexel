// abs358@drexel.edu

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int DEBUG = 0;

enum {
	Nbuiltins = 1,
	Nbuf = 512,
	Ncommands = 16,
	Nargs = 16,
	Nbackground = 16
};
struct command {
	int opcode; // 1=normal, 2=background, 3=piped
	int argc;
	char *argv[Nargs];
};
char *prompt;
const char *const builtins[Nbuiltins] = {"cd"};

char getinput(char *input);
int parse(char *input, struct command commands[Ncommands]);
void display(struct command commands[Ncommands]);
int execute(struct command commands[Ncommands]);

int
main(int argc, char *argv[])
{
	struct command commands[Ncommands];
	char buf[Nbuf];
	
	prompt = "mysh: ";
	while (1) 
	{
		printf("%s", prompt);
		if (getinput(buf) == '\0') { printf("\n"); break; }
// printf("buf = %s\n", buf);
// printf("buf = %p\n", buf);
		parse(buf, commands);
		display(commands);
	}
	exit(0);
}

char
getinput(char *input)
{
	char *temp;
	
	memset(input, '\0', sizeof(char) * Nbuf);
	fgets(input, sizeof(char) * Nbuf, stdin);
	if (NULL != (temp = strchr(input, '\n'))) { *(temp) = '\0'; } // remove trailing newline
	return *input;
}

int
parse(char *input, struct command commands[Ncommands])
{
	int commandnum, argnum, charnum, previousNULL, opcode;

	commandnum = 0;
	argnum = -1;
	charnum = -1;
	previousNULL = 1;
	opcode = 0;
	
	while (input[++charnum] != '\0') {
// printf("input[%d] = %d = %c\n", charnum, input[charnum], input[charnum]);
		switch (input[charnum]) {
			case ' ':
				input[charnum] = '\0';
				previousNULL = 1;
				break;
			case ';':
				opcode = 1;
				break;
			case '&':
				opcode = 2;
				break;
			case '|':
				opcode = 3;
				break;
			default:
				if (previousNULL) {
// printf("\tNew arg %d in command %d\n", argnum+1, commandnum);
					commands[commandnum].argv[++argnum] = input + charnum;
					previousNULL = 0;
				}
		}
		
		if (opcode) {
// printf("\tNew command\n");
			commands[commandnum].opcode = opcode;
			commands[commandnum++].argc = ++argnum;
			commands[commandnum].opcode = 0; // preset empty command
			argnum = -1;
			input[charnum] = '\0';
			previousNULL = 1;
			opcode = 0;
		}

	}
	
	if (argnum != -1) { // no cmd-terminating char
		commands[commandnum].opcode = 1; // assume normal execution
		commands[commandnum++].argc = ++argnum;
		commands[commandnum].opcode = 0;
	}
}

void
display(struct command commands[Ncommands])
{
	int commandnum, argnum;
	
	for (commandnum = 0; commands[commandnum].opcode != 0; commandnum++) {
		printf("Command[%d]:\n", commandnum);
		printf("\topcode = %d\n", commands[commandnum].opcode);
		printf("\targc = %d\n", commands[commandnum].argc);
		for (argnum = 0; argnum < commands[commandnum].argc; argnum++) {
			printf("\targv[%d] = %p = %s\n", argnum, commands[commandnum].argv[argnum], commands[commandnum].argv[argnum]);
		}
	}
}
/*
int
__execute(struct command commands[Ncommands])
{
	int i, pid, status, background;
	const useconds_t patience = 10;
	
	if (DEBUG > 0) { printf("test: runcommand() start\n"); }

	// look for builtin commands
	if (DEBUG > 1) { printf("test: runcommand() builtin check\n"); }
	for (i = 0; argv[0] != NULL && i < Nbuiltins; i++) {
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
*/
