def is_prime(n):
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True

def sieve(k):
    i = 2
    while i * i <= k:
        if k % i != 0:
            return False

        # DO WHILE
        while True:
            i += 1
            if is_prime(i):
                break
    return True


if __name__ == "__main__":
    k = int(input("Insert k: "))
    print(sieve(k))