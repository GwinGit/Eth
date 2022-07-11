#include <stdio.h>

int flag;

int main(int argc, char **argv)
{
	char buffer[] = "AAAAAAAABBBBBBBBAAAAAAAABBBBBBBBAAAAAAAABBBBBBBB";
	char buf2[] = "\xde\xad\xde\xad\xca\xfe\xca\xfe";
	if (argc < 1) {
		printf("Please, enter yout name!\n");
	}

	printf(argv[1]);

	if (flag) {
		printf("\n\nYou win!\n");
	} else {
		printf("\n\nI am sorry! Try again!");
	}

	return 0;
}
