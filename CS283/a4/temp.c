#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int
main()
{
	char *args[2];
	args[0] = "fruit";
	args[1] = NULL;

	printf("temp.c\n");
	execvp("./cclist", args);
	printf("fuck\n");
}
