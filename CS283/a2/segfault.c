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
	// P1
	int buf[10];
	unsigned int i;
	// P2
	char *str;
	char *printThisOne;
	// P3
	char *word;
	// P4
	int *integers;
	// P8
	int foo;
	// P9
	int *bar;
	// P10
	char *someText;

	// P1
	for (i = 0; i < 10; ++i) {
		buf[i] = i;
	}
	for (i = 0; i < 10; ++i) {
		printf("Index %d = %d\n", i, buf[i]);
	}
	/* Error:
		Printf had the wrong formatting for its arguments
		The for loops were extending to buf[10] but buf[9] was the last word allocated
	 */
	// P2
	str = malloc(sizeof(char) * 19);
	strcpy(str, "Something is wrong");
	printf("%s\n", printThisOne = str);
	/* Error
		We need more than 10 bytes for str (18 chars + 1 null char)
		In order to print the string pointed to by str while technically printing the printThisOne variable, we need to have printThisOne point to the same memory location
	 */

	// P3
	word = malloc(sizeof(char) * 7);
	strcpy(word, "Part 3");
	*(word + 4) = '-';
	printf("%s\n", word);
	free(word);
	/* Error:
		Bc the string pointed to by word could be in read-only memory (in this case it is), we need to make sure it's stored in the heap instead
	 */

	// P4
	integers = malloc(sizeof(int) * 11);
	*(integers + 10) = 10;
	printf("Part 4: %d\n", *(integers + 10));
	free(integers);
	/* Error:
		Integers was not assigned to an allocated spot in memory
		Alternatively the declaration could include an array of size at least 11
	 */

	// P5
	printf("Print this whole line\n");
	/* Error:
		The null character was in the string so the string which is a no no
	 */

	long int x;
	x = 2147483647;
	printf("%ld is positive\n", x); 
	x += 1000000000;
	printf("%ld is positive\n", x); 
	/* Error:
		x was never initialized
		x needs to be a long bc after the addition there would be an overflow error
	 */

	// P7
	printf("Cleaning up memory from previous parts\n");
	free(str);
	//free(buf)
	/* Error:
		buf is on the stack so it can't be freed
	 */

	// P8
	fib(&foo, 7);
	printf("fib(7) = %d\n", foo);
	/* Error:
		foo needed to be passed as a reference
	 */

	// P9
	//bar = 0;
	bar = malloc(sizeof(int) * 1);
	*bar = 123;
	printf("bar = %d\n", *bar);
	/* Error:
		In setting bar to 0, we can't be sure that memory location 0 is allocated to this program
		When compiling and running on local WSL Ubuntu, there were no errors with commenting out that line but on tux there was so I just added the malloc to handle it more explicitly
	 */

	// P10
	someText = malloc(10);
	strcpy(someText, "testing");
	printf("someText = %s\n", someText);
	free(someText);
	/* Error:
		We tried freeing someText before our last use of it!
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
