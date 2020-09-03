// abs358@drexel.edu

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/wait.h>

enum {
	Nbuiltins = 1,
	Nbuf = 512,
	Ncommands = 16,
	Nargs = 16,
	Nbackground = 16
};
struct command {
	int argc;
	char *argv[Nargs];
	int opcode; // 1=normal, 2=background, 3=piped
	char *redirect_in;
	char *redirect_out;
	char *redirect_append;
};
char *prompt;
const char *const builtins[Nbuiltins] = {"cd"};

char getinput(char *input);
int parse(char *input, struct command commands[Ncommands]);
void display(struct command commands[Ncommands]);
int execute(struct command commands[Ncommands]);

int
main()
{
	struct command commands[Ncommands];
	char buf[Nbuf];
	
	prompt = "mysh: ";
	while (1) 
	{
		printf("%s", prompt);

		if (getinput(buf) == '\0') { printf("\n"); break; }
		parse(buf, commands);
		// display(commands);

		execute(commands);
	}
	exit(0);
}

char
getinput(char *input)
{
	char *temp;
	
	memset(input, '\0', sizeof(char) * Nbuf);
	fgets(input, sizeof(char) * Nbuf, stdin);
	if (NULL != (temp = strchr(input, '\n'))) {
		*(temp) = '\0'; // remove trailing newline
		return '\n';
	} 
	return *input;
}

int
parse(char *input, struct command commands[Ncommands])
{
	int commandnum, argnum, charnum;
	int previousNULL, opcode, r_in, r_out, r_append;

	// initialize commands
	for (commandnum = 0; commandnum < Ncommands; commandnum++) {
		commands[commandnum].opcode = 0;
		commands[commandnum].argc = 0;
		for (argnum = 0; argnum < Nargs; argnum++) {
			commands[commandnum].argv[argnum] = (char *)NULL;
		}
		commands[commandnum].redirect_in = (char *)NULL;
		commands[commandnum].redirect_out = (char *)NULL;
		commands[commandnum].redirect_append = (char *)NULL;
	}

	commandnum = 0;
	argnum = -1;
	charnum = -1;
	previousNULL = 1;
	opcode = 0;
	r_in = 0;
	r_out = 0;
	r_append = 0;
	
	while (input[++charnum] != '\0') {
//printf("input[%d] = %d = %c\n", charnum, input[charnum], input[charnum]);
		switch (input[charnum]) {
			// argument terminator
			case ' ':
				input[charnum] = '\0';
				previousNULL = 1;
				break;
			// command terminators
			case ';':
				opcode = 1;
				break;
			case '&':
				opcode = 2;
				break;
			case '|':
				opcode = 3;
				break;
			// I/O redirection
			case '<':
				input[charnum] = '\0';
				r_in = 1;
				break;
			case '>':
				input[charnum] = '\0';
				r_append += r_out;
				r_out = ++r_out % 2;
				break;
			default:
				if (r_in) {
//printf("\tNew redirect_in for command %d\n", commandnum);
					commands[commandnum].redirect_in = input + charnum;
					r_in = 0;
					previousNULL = 0;
				}
				if (r_out) {
//printf("\tNew redirect_out for command %d\n", commandnum);
					commands[commandnum].redirect_out = input + charnum;
					r_out = 0;
					previousNULL = 0;
				}
				if (r_append) {
//printf("\tNew redirect_append for command %d\n", commandnum);
					commands[commandnum].redirect_append = input + charnum;
					r_append = 0;
					previousNULL = 0;
				}
				if (previousNULL) {
//printf("\tNew arg %d in command %d\n", argnum+1, commandnum);
					commands[commandnum].argv[++argnum] = input + charnum;
					previousNULL = 0;
				}
		}
		if (opcode) { // same behavior for all opcodes
// printf("\tNew command\n");
			commands[commandnum].opcode = opcode;
			commands[commandnum++].argc = ++argnum;
			argnum = -1;
			input[charnum] = '\0';
			previousNULL = 1;
			opcode = 0;
		}
	}
	if (argnum != -1) { // last cmd lacks terminating character
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
		if (commands[commandnum].redirect_in != NULL) { printf("\tredirect_in = %s\n", commands[commandnum].redirect_in); }
		if (commands[commandnum].redirect_out != NULL) { printf("\tredirect_out = %s\n", commands[commandnum].redirect_out); }
		if (commands[commandnum].redirect_append != NULL) { printf("\tredirect_append = %s\n", commands[commandnum].redirect_append); }
	}
}

int
execute(struct command commands[Ncommands])
{
	int i, j, pid, status, fd, pfd[Ncommands][2];
	
	for (i = 0; commands[i].argc > 0; i++) {
		// builtin commands don't require forking
		for (j = 0; j < Nbuiltins; j++) { if (0 == strcmp(commands[i].argv[0], builtins[j])) { break; } }
		if (j < Nbuiltins){
			switch (j) {
				case 0: // "cd"
					if (commands[i].argv[1] == NULL) {
						chdir(getenv("HOME"));
					}
					else if (0 != chdir(commands[i].argv[1])){
						printf("cd failed - directory has not been changed\n");
					}
					break;
				// no other builtins right now
			}
			continue; // on to the next command
		}
		// not a builtin command - proceediing with regularly scheduled programming
		// pipe
		pipe(pfd[i]);
		// fork
		if ((pid = fork()) < 0) { perror("fork"); break; }
		// child
		if (pid == 0) {
			// redirection
			if (commands[i].redirect_in != NULL) {
				fd = open(commands[i].redirect_in, O_RDONLY);
				if (fd < 0) {
					perror("open - redirect_in");
					exit(3);
				}
				dup2(fd, 0);
				close(fd);
			}
			if (commands[i].redirect_out != NULL) {
				fd = open(commands[i].redirect_out, O_TRUNC | O_CREAT | O_WRONLY, 0664);
				if (fd < 0) {
					perror("open - redirect_out");
					exit(3);
				}
				dup2(fd, 1);
				close(fd);
			}
			if (commands[i].redirect_append != NULL) {
				fd = open(commands[i].redirect_append, O_APPEND | O_CREAT | O_WRONLY, 0664);
				if (fd < 0) {
					perror("open - redirect_append");
					exit(3);
				}
				dup2(fd, 1);
				close(fd);
			}
			// piping overrides redirection
			if (i > 0 && commands[i-1].opcode == 3) { // reciever
				dup2(pfd[i-1][0], 0);
				close(pfd[i-1][0]);
			}
			if (commands[i].opcode == 3) { // sender
				dup2(pfd[i][1], 1);
				close(pfd[i][0]);
				close(pfd[i][1]);
			}
			// execute
			execvp(commands[i].argv[0], commands[i].argv);
			perror("execvp - child");
			exit(1);
		}
		// parent
		if (pid > 0) {
			// close irrelevant fds
			close(pfd[i][1]);
			close(pfd[i-1][0]);
			// serialize piped commands
			if (commands[i].opcode != 2) {
				waitpid(pid, &status, 0);
			}
		}
	}
}

