#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool is_prime(int n) {
    for (int i = 2; i < n; i++)
    {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

bool sieve(int n) {
    int i = 2;
    while (i * i <= n)
    {
        if (n % i == 0)
        {
            return false;
        }
        
        do
        {
            i++;
        } while (!is_prime(i));
    }
    return true;
}

int main() {
    int n;

    printf("Insert a number (>=2)\n>");
    scanf("%d", &n);
    
    printf("The number is %sprime", sieve(n) ? "" : "not ");

    printf("\n\n");
    return 0;
}