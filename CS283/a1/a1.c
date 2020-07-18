// Adin Solomon - July 2020
// abs358@drexel.edu

#include <stdio.h>
#include <stdlib.h>

// Image data
char *image;
int i_width, i_height, max;

// Thumbnail data
char *thumbnail;
int scale_factor, t_width, t_height;

// Hepful functions - separated for maintenance and further development
char reduce( char *square ); // if I want to change the reduce method
char *getsquare( int square_num ); // if I want to change the system of sectioning

int
main()
{
	int i;

	// Extract information from the header
	if (scanf("P5 %d %d %d", &i_width, &i_height, &max) != 3) {
		perror("scanf");
		exit(1);
	}

	// Read the image from stdin
	if ((image = malloc( i_width * i_height )) == NULL) {
		perror("image malloc");
		exit(2);
	}
	if (fread(image, 1, i_width*i_height, stdin ) != i_width*i_height) {
		perror("fread");
		exit(3);
	}

	// Allocate Space for thumbnail
	scale_factor = ((i_width > i_height) ? i_width : i_height) / 200;
	t_width = i_width / scale_factor;
	t_height = i_height / scale_factor;
	if ((thumbnail = malloc( t_width*t_height )) == NULL) {
		perror("thumbnail malloc");
		exit(4);
	}

	// Iterate over sections of the image, reduce, then add to thumbnail
	for (i = 0; i < t_width*t_height; i++) {
		*(thumbnail + i) = reduce(getsquare(i));
	}

	// Write out the thumbnail
	if (printf("P5\n%d %d\n%d", t_width, t_height, max) < 6) {
		perror("printf");
		exit(5);
	}
	if (fwrite( thumbnail, 1, t_width*t_height, stdout ) < t_width*t_height) {
		perror("fwrite");
		exit(6);
	}
	exit(0);
}

char
reduce( char *square ) {
	int i;

	for (i = 0; i < scale_factor*scale_factor; i++) {
		*square = ( *square / 2 ) + ( *(square + 1) / 2 ); // avoid overflow errors
	}

	return *square;
}

char *
getsquare( int square_num ) {
	char *square, *sq_ptr;
	int i, j;

	sq_ptr = image;
	sq_ptr += i_width * ((square_num / t_width) * scale_factor); // shift by 'rows'
	sq_ptr += (square_num % t_width) * scale_factor; // shift by 'columns'

	square = malloc(scale_factor * scale_factor);
	for (i = 0; i < scale_factor; i++) {
		for ( j = 0; j < scale_factor; j++ ){
			*(square + (i * scale_factor) + j) = *(sq_ptr + (i * i_width) + j);
		}
	}

	return square;
}
