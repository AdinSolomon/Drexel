/*
   This assignment is to help you learn how to debug
   compiler warnings/errors and other common errors
   in your code. For each part labeled P(n), there is
   a warning/error/problem that goes with it. Write
   down what the issue was in the `Error:` section of
   each problem. Submit `segfault.c` along with your
   fixes and error comments.
 */

// P0
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/* Error:
	We needed to include string.h to use strcpy()
 */

void fib(int* A, int n);

int
main(int argc, char *argv[]) {
	int buf[10];
	unsigned int i;
	char *str;
	char *printThisOne;
	char *word;
	int *integers;
	int foo;
	int *bar;
	char *someText;

	printf("P1\n");
	// P1
	for (i = 0; i < 10; ++i) {
		buf[i] = i;
	}
	for (i = 0; i < 10; ++i) {
		printf("Index %d = %d\n", i, buf[i]);
	}
	/* Error:
		Compiling Error:
			printf had the wrong formatting for its arguments
		Runtime Error:
			the for loops were extending to buf[10] but buf[9] was the last word allocated
	 */
	printf("P2\n");
	// P2
	str = malloc(sizeof(char) * 1000);
	strcpy(str, "Something is wrong");
	printf("%s\n", printThisOne);
	/* Error:
		the second argument in strcpy (including the null character) is longer than 10, the original number of character malloced into str
	 */

	printf("P3\n");
	// P3
	word = "Part 3....";
	*(word + 4) = '-';
	printf("%s\n", word);
	/* Error:

	 */

	printf("P4\n");
	// P4
	*(integers + 10) = 10;
	printf("Part 4: %d\n", *(integers + 10));
	free(integers);
	/* Error:

	 */

	printf("P5\n");
	// P5
	printf("Print this whole line\n");
	/* Error:
		The null character was in the string
	 */

	printf("P6\n");
	// P6
	int x;	// bad style but it's only for this section
	x = 2147483647;
	printf("%d is positive\n", x); 
	x += 1000000000;
	printf("%d is positive\n", x); 
	/* Error:
	 	Compilling Error:
			x was never initialized
		Runtime Error:
			
	 */

	printf("P7\n");
	// P7
	printf("Cleaning up memory from previous parts\n");
	free(str);
	/* Error:
		buf is on the stack so it can't be freed
	 */

	printf("P8\n");
	// P8
	fib(&foo, 7);
	printf("fib(7) = %d\n", foo);
	/* Error:
		Compilling Error:
			foo needed to be passed as a reference
	 */

	printf("P9\n");
	// P9
	bar = 0;
	*bar = 123;
	printf("bar = %d\n", *bar);
	/* Error:

	 */

	// P10
	someText = malloc(10);
	strcpy(someText, "testing");
	free(someText);
	printf("someText = %s\n", someText);
	/* Error:

	 */

	exit(0);
}

// fib calculates the nth fibonacci number and puts it in A.
// There is nothing wrong with this function.
void fib(int *A, int n)
{
	int temp;
	if (n == 0 || n == 1)
		*A = 1;
	else {
		fib(A, n - 1);
		temp = *A;
		fib(A, n - 2);
		*A += temp;
	}
}
