#include <stdio.h>

#define F_LEN 10

int main(int argc, char** argv) {

	char f[F_LEN];

	fgets(f, F_LEN, stdin);
	
	
	int i;
	short ok = 1;
	for (i = 0; i < F_LEN - 1; i++)
		if (f[i] != '0' + i) {
			ok = 0;
			break;
		}

	if (ok)
		puts("Yeah!");
	else
		puts("Nope");

	return 0;
}
