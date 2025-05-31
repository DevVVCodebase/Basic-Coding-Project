#include<stdio.h>
#include <conio.h>
int cacl(int calc, int a, int b)
{
    switch(calc){
        case 1: printf("%d\n", a+b);
                break;
        case 2: printf("%d\n", a-b);
                break;
        case 3: printf("%d\n", a*b);
                break;
        case 4: 
            if (b == 0)
            {
                printf("Error: Division by zero!\n");
            }
            else
            {
                printf("%f\n", (float)a / b);
                break;
            }

        default:
            printf("Invalid operation!\n");   
            return 0;
    }
    return 0;
}

void main()
{
    char yes;
    do{
        int calc, a, b;
        printf("Enter the first number: ");
        scanf("%d",&a);
        printf("Enter the second number: ");
        scanf("%d",&b);

        printf("For addition(+): 1\nFor subtraction(-): 2\nFor multiplication(*): 3\nFor division(/): 4\n");
        scanf("%d",&calc);

        cacl(calc, a, b);

        printf("Do you want to continue (y/n)? ");
        scanf(" %c", &yes);
    }while( yes =='y');
    getch();
}