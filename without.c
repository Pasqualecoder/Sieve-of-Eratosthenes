#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool is_prime(long long n)
{
    for (long long i = 2; i < n; i++)
    {
        if (n % i == 0)
        {
            return false;
        }
    }
    return true;
}

int main()
{
    int test_cases;
    long long k;
    scanf("%lld", &test_cases);

    while (test_cases--)
    {
        scanf("%lld", &k);
        printf("%d %s\n", k, is_prime(k) ? "True" : "False");
    }

    return 0;
}
