#include <stdio.h>
void main() {
	int value1 = 5, value2 = 15;
	int* p1, * p2;
	p1 = &value1;
	p2 = &value2;
	*p1 = 10;
	*p2 = *p1;
	p1 = p2;
	*p1 = 20;
	printf("value1 == %d and value2 == %d", value1, value2);
}