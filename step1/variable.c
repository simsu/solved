#include <stdio.h>
 
void ex1()
{
    int a,b;
    printf("A >> ");
    scanf("%d", &a);
    printf("B >> ");
    scanf("%d", &b);
    printf("%d\n",a+b);
}

void ex2()
{
   int b, h;
    b = 20;
    h = 15;

    printf("*** 삼각형 면적 구하기 ***\n");
    printf("면적 = 밑변 * 높이 / 2 = %d * %d / 2\n = %d\n", b, h, b*h/2);
}

void ex3()
{
    printf("7 / 5 = %d\n", 7/5);
    printf("7 / 5.0 = %f\n", 7 / 5.0);
    printf("7.0 / 5.0 = %f\n", 7.0 / 5.0);
}

void ex4()
{
    int total, cnt;
    float avg;
 
    total = 215;
    cnt = 10;
 
    avg = (float)total / cnt;
 
    printf("%.2f\n", avg);
}

int main()
{
    // ex1();
    // ex2();
    // ex3();
    ex4();
   return 0;
}