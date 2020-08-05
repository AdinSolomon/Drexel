// abs358@drexel.edu

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/file.h>
#include <sys/types.h>
#include <sys/stat.h>
#include "cc.h"

char *rmNewLine(char *str);

int
main(int argc, char *argv[])
{
	int id;
	struct stat ccstat;
	CComp comp;
	char buf[sizeof(CComp)];
	FILE *fp;
	
	if(argc != 2) {
		fprintf(stderr, "Usage: ccitem id\n");
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
	// open the file, get the struct, then go through attributes
	if((fp = fopen("ccomp.db", "r+")) == NULL) {
		fprintf(stderr, "fopen\n");
		exit(4);
	}
	flock(fileno(fp), LOCK_EX);
	fseek(fp, id * sizeof(CComp), SEEK_SET);
	fread(&comp, sizeof(CComp), 1, fp);
	// If the item was deleted, then do nothing
	if(comp.id != id) {
		exit(0);
	}
	// Get input from stdin
	printf("Editing item #%d. For each attribute, enter either nothing for no change or the new value.\n", id);
	printf("Maker:\n\t%s\n\t", comp.maker);
	fgets(buf, Nmaker, stdin);
	if(strlen(rmNewLine(buf)) > 0) {
		strcpy(comp.maker, buf);
	}
	printf("Model:\n\t%s\n\t", comp.model);
	fgets(buf, Nmodel, stdin);
	if(strlen(rmNewLine(buf)) > 0) {
		strcpy(comp.model, buf);
	}
	printf("Year:\n\t%d\n\t", comp.year);
	fgets(buf, sizeof(CComp), stdin);
	if(strlen(rmNewLine(buf)) > 0) {
		comp.year = atoi(buf);
	}
	printf("CPU:\n\t%s\n\t", comp.cpu);
	fgets(buf, Ncpu, stdin);
	if(strlen(rmNewLine(buf)) > 0) {
		strcpy(comp.cpu, buf);
	}
	printf("Description:\n\t%s\n\t", comp.desc);
	fgets(buf, Ndesc, stdin);
	if(strlen(rmNewLine(buf)) > 0) {
		strcpy(comp.desc, buf);
	}
	fseek(fp, id * sizeof(CComp), SEEK_SET);
	fwrite(&comp, sizeof(CComp), 1, fp);
	flock(fileno(fp), LOCK_UN);
	fclose(fp);
	exit(0);
}

char *
rmNewLine(char *str)
{
	int i = 0;
	while(1) {
		if(str[++i] == '\0') {
			str[i-1] = '\0';
			return str;
		}
		
	}
}



