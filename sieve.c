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

bool sieve(long long n)
{
    long long i = 2;
    while (i * i <= n)
    {
        if (n % i == 0)
        {
            return false; // the number is NOT prime
        }

        do
        {
            i++;
        } while (!is_prime(i));
    }
    return true; // the number is prime
}

int main()
{
    int test_cases;
    long long k;
    scanf("%lld", &test_cases);

    while (test_cases--)
    {
        scanf("%lld", &k);
        printf("%d %s\n", k, sieve(k) ? "True" : "False");
    }

    return 0;
}
