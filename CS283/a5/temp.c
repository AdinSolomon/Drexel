
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

char *rmnewline(char *str);

int
main()
{
	char *input;

	input = malloc(sizeof(char) * 512);
	input[0] = '\0';
	printf("give me something pls\n");
	fgets(input, sizeof(char) * 512, stdin);
	rmnewline(input);
	
	if (chdir(input) == -1) { printf("fruit\n"); }

	exit(0);
}

char *
rmnewline(char *str)
{
	int i = -1;
	while(str[++i] != '\n') {}   
	str[i] = '\0';
	return str;
} 
