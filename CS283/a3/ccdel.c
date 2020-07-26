// abs358@drexel.edu

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/file.h>
#include <sys/stat.h>
#include <sys/types.h>
#include "cc.h"

int
main(int argc, char *argv[]) 
{
	int id;
	int newid;
	struct stat ccstat;
	FILE *fp;

	if(argc != 2) {
		fprintf(stderr, "Usage: ccdel id\n");
		exit(1);
	}
	id = atoi(argv[1]);
	// Ensure that id isn't out of range
	if(stat("ccomp.db", &ccstat) < 0) {
		fprintf(stderr, "stat\n");
		exit(2);
	}
	if(id > ccstat.st_size / sizeof(CComp) - 1) {
		fprintf(stderr, "id out of range\n");
		exit(3);
	}
	// Change id to -1 to indicate it has been removed
	if((fp = fopen("ccomp.db", "r+")) == NULL) {
		fprintf(stderr, "fopen\n");
		exit(4);
	}
	flock(fileno(fp), LOCK_EX);
	fseek(fp, id * sizeof(CComp) + Nmaker + Nmodel + sizeof(int) + Ncpu, SEEK_SET);
	newid = -1;
	fwrite(&newid, sizeof(int), 1, fp);
	flock(fileno(fp), LOCK_UN);
	fclose(fp);
	exit(0);
}
