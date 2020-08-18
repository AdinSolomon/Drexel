#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

enum {
	Nbuf = 2048,
	Ncommands = 16,
	Nargs = 32
};

struct command {
	int optype; /* 1=normal; 2=background; 3=piped */
	int argc;
	char *argv[Nargs];
};

int
main(int argc, char *argv[])
{
	struct command commands[Ncommands];
	char buf[Nbuf];
	int commandnum, argnum, charnum, previousNULL;
	
	printf("pls give me an input line\n");
	fgets(buf, Nbuf, stdin);
	{
		char *temp;
		if (NULL != (temp = strchr(buf, '\n'))) { *(temp) = '\0'; } // remove trailing newline
	}
	printf("you entered \"%s\"\n", buf);
	
	// initialize the counts and flags
	commandnum = 0;
	argnum = -1;
	charnum = -1;
	previousNULL = 1;

	while (buf[++charnum] != '\0') {
		printf("Evaluating buf[%d] = %c = %d:\n", charnum, buf[charnum], buf[charnum]);
		switch (buf[charnum]) {
			case ' ':
				printf("\tIt's a space\n");
				buf[charnum] = '\0';
				previousNULL = 1;
				break;
				
			case ';':
				printf("\tIt's a semicolon\n");
				commands[commandnum].optype = 1; // normal execution
				commands[commandnum++].argc = ++argnum;
				argnum = -1;
				buf[charnum] = '\0';
				previousNULL = 1;
				break;

			case '&':
				printf("\tIt's an ampersand\n");
				commands[commandnum].optype = 2; // background execution
				commands[commandnum++].argc = ++argnum;
				argnum = -1;
				buf[charnum] = '\0';
				previousNULL = 1;
				break;

			case '|':
				printf("\tIt's a pipe\n");
				commands[commandnum].optype = 3; // piped execution
				commands[commandnum++].argc = ++argnum;
				argnum = -1;
				buf[charnum] = '\0';
				previousNULL = 1;
				break;
			
			default:
				printf("\tDefault case\n");
				if (previousNULL) {
					printf("\tNew arg in command %d\n", commandnum);
					commands[commandnum].argv[++argnum] = buf + charnum;
					previousNULL = 0;
				}
			}
	}
	// check for no command-terminating character
	if (argc != -1) {
		commands[commandnum].optype = 1; // assume normal execution
		commands[commandnum].argc = ++argnum;
	}
	
	// print results
	printf("\ndone\n");
	for (int i = 0; i <= commandnum; i++) {
		printf("Command %d:\n", i);
		printf("\toptype = %d\n", commands[i].optype);
		printf("\targc = %d\n", commands[i].argc);
		for (int j = 0; j < commands[i].argc; j++) {
			printf("\targv[%d] = %p = %s\n", j, commands[i].argv[j], commands[i].argv[j]);
		}
	}
	exit(0);
}
