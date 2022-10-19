def is_prime(n):
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True

if __name__ == "__main__":
    test_cases = int(input())
    for i in range(test_cases):
        k = int(input())
        print(k, is_prime(k))
