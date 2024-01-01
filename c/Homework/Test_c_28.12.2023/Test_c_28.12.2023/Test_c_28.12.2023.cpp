#include <stdio.h>

void calculator(int get_num) {
	int num, smaalest = 9, bigest = 0;

	while (get_num > 0)
	{
		num = get_num % 10;
		get_num = get_num / 10;

		if (num > bigest)
			bigest = num;
		if (num < smaalest)
			smaalest = num;
	}
	printf("The difference between the largest and smallest number is: %d\n\n", bigest - smaalest);
}

void dividing(int num1,int num2) {

	int divider, check = num2;

	while (check > 0)
	{
		if (num1 % check == 0 && num2 % check == 0)
			printf("%d ", check);
		check--;
	}
}

void polindrom(int chars[], int arr_size) {

	int i;
	bool status;
	for (i = 0; i < arr_size; i++) {
		if (chars[i] == chars[arr_size - i])
			status = true;
		else
		{
			status = false;
			break;
		}
	}
	if (status == true)
		printf("it's a polindrom!\n\n");
	else
		printf("it's not a polindrom!\n\n");
}





void main() {
	//calculator(12345678);
	
	//dividing(4, 20);

	//int a[] = {1, 3, 2, 3, 1};
	//int arr_size = (sizeof(a) / sizeof(int))-1;
	//polindrom(a, arr_size);


}