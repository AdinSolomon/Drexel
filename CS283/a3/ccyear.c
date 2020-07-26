// abs358@drexel.edu

#include <stdio.h>
#include <stdlib.h>
#include <sys/file.h>
#include "cc.h"

int
main(int argc, char *argv[])
{
	CComp comp;
	int index;
	FILE *fp;
	
	if(argc != 3) {
		fprintf(stderr, "Usage: ccyear start end\n");
		exit(1);
	}
	fp = fopen("ccomp.db", "r");
	if(fp == NULL) {
		fprintf(stderr, "fopen\n");
		exit(3);
	}
	flock(fileno(fp), LOCK_SH);
	index = 1;
	fseek(fp, sizeof(CComp), SEEK_SET);
	while(fread(&comp, sizeof(CComp), 1, fp) > 0) {
		if(index == comp.id && 
			((atoi(argv[1]) <= comp.year && comp.year <= atoi(argv[2])) ||
			 (atoi(argv[1]) >= comp.year && comp.year >= atoi(argv[2])))) {
			printf("\n");
			printf("Maker: %s\n", comp.maker);
			printf("Model: %s\n", comp.model);
			printf("Year: %d\n", comp.year);
			printf("CPU: %s\n", comp.cpu);
			printf("Id: %d\n", comp.id);
			printf("Desc: %s\n", comp.desc);
			printf("----------------\n");
		}
		index++;
	}
	flock(fileno(fp), LOCK_UN);
	fclose(fp);
	exit(0);
}
