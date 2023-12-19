#include <stdio.h>


int main(){

	int num;

	//get num
	printf("Enter a number: ");
	scanf_s("%d", &num);

	int max_num = 0, min_num = num, i = 0;

	// do whail in the same times thet you get

	while (num > 0)
	{
		i = num % 10;

		if (i > max_num)
			max_num = i;

		else if (i < min_num)
			min_num = i;

		
		num = num / 10;
	}

	printf("\nThe largest number is %d \nThe smallest number is %d \nThe difference between them is %d\n\n", max_num, min_num, max_num - min_num);

	



}