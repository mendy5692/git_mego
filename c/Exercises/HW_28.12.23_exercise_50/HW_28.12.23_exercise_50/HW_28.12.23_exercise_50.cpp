#include <stdio.h>
#define SIZE 7
#include < stdlib.h >
#include < time.h>

void main() {

	srand(time(0));

	int i;
	int num_array[] = { 1,2,3,4,5,6,7 };

	int* ptr;

	ptr = &num_array[rand()%7];

	for (i = 0; i < 10; i++) {
		ptr = &num_array[rand() % 7];
		printf("%d ", *ptr);
	}




}