#include <stdio.h>
#include <math.h>

void ex1()
{
    printf("Hello !!!\nHow are you?\nFine thank you.\n");
}
void ex2()
{
    int i = 0;
    double j = 4;
    int k = 1;
    for (j=4; j>0; j--)
    {
        for(i=0; i<j-1; i++)
        {
            printf(" ");
        }
        for (i=0; i<k; i++)
        {
            printf("*");
        }
        for(i=0; i<j-1; i++)
        {
            printf(" ");
        }
        k+=2;
    printf("\n");
    }
}

int main()
{
    ex1();
    ex2();
    return 0;
}