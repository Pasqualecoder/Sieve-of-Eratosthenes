def is_prime(n):
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True

def next_prime(n):
    while True:
        n += 1
        if is_prime(n):
            break
    return n

def sieve(k):
    i = 2
    while i * i <= k:
        if k % i == 0:
            return False # the number is NOT prime
        i = next_prime(i)   
    return True # the number is prime


if __name__ == "__main__":
    test_cases = int(input())
    for i in range(test_cases):
        k = int(input())
        print(k, sieve(k))
