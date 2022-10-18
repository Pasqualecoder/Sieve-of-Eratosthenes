# <a href="https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes">Sieve of Eratosthenes</a>

> **Teorema**: Sia n un numero naturale, n >= 2. Allora n è primo se non ammette alcun divisiore primo p con p^2 <= n.

> **Theorem**: Given n, natural number >= 2. n is a prime number if it has no prime divisor with p^2 <= n.

> Example: <br>
n = 151. We want to find out if it is a prime number. <br>
2 -> 2^2 <= 151 (true) but 2 doesn't divide <br>
3 -> 3^2 <= 151 (true) but 3 doesn't divide 151 <br>
5 -> 5^2 <= 151 (true) but 5 doesn't divide 151 <br>
... <br>
13 -> 13^2 <= 151 (FALSE)... STOP <br>
151 is a prime number because every prime, with square <=151, doesn't divide 151. <br>
---

*Find prime number between 2 and k (extrems inluded),
with and without Sieve of Eratosthenes*

Input:
100

Output:
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97


N.B. 1 is not prime.