#include <stdio.h>
#define SIZE 7

void main() {

	int num_array[] = { 1,2,3,4,5,6,7 };

	int i = 0;

	int* ptr;

	ptr = &num_array[6];

	for (i = 0; i < SIZE; i++) {
		printf("%d ", *ptr--);
	}


}