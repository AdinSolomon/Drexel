// from bls96@drexel.edu

#include <stdio.h>
#include <stdlib.h>
#include <sys/file.h>
#include "cc.h"

int
main(int argc, char *argv[])
{
	CComp target;
	FILE *fp;
	int index;
	int n;

	if(argc != 2) {
		fprintf(stderr, "Usage: ccitem id\n");
		exit(1);
	}
	fp = fopen("ccomp.db", "r+");
	if (fp == NULL) {
		fprintf(stderr, "fopen\n");
		exit(2);
	}
	flock(fileno(fp), LOCK_SH);
	index = atoi(argv[1]);
	fseek(fp, index * sizeof(CComp), SEEK_SET);
	n = fread(&target, sizeof(CComp), 1, fp);
	flock(fileno(fp), LOCK_UN);
	fclose(fp);
	if(n <= 0 || index != target.id) {
		fprintf(stderr, "No such item\n");
		exit(3);
	}
	printf("Maker: %s\n", target.maker);
	printf("Model: %s\n", target.model);
	printf("Year: %d\n", target.year);
	printf("CPU: %s\n", target.cpu);
	printf("Id: %d\n", target.id);
	printf("Desc: %s\n", target.desc);
	exit(0);
}
