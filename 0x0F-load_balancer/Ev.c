
#include <stdio.h>
/**
 * main - interview  Question
 * Return: 0
 */
int main(void)
{
	int start = 1, end = 6;
	char c = 'E';

	while (start <= end)
	{
		printf("%c \n", c);
		/*Answer line */
		c = (c == 69) ? (c + 32) : (c - 32);
		start++;

	}
		return (0);
}

