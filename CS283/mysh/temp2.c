
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

char *rmnewline(char *str);

int
main()
{
	unsigned char c, *input = malloc(sizeof(char) * 256);
	
	c = fgetc(stdin);
	printf("%d\n", c);
} 
