#include <stdio.h>

int main()
{
    int a, b;
    for(;;)
    {
        printf("===============\n두 수 입력 : (끝내려면 0 0 입력)\n===============\n");
        scanf("%d %d", &a, &b);
        if(a == 0 && b == 0)
        {
            break;
        }
        printf("%d + %d = %d\n", a, b, a+b);
        if(a > b)
        {
            printf("큰 수 : %d\n", a);
            continue;
        } else if(a < b) {
            printf("큰 수 : %d\n", b);
        } else {
            printf("두 수는 같습니다.\n");
        }
    }
    return 0;
}