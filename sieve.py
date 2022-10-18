def is_prime(n):
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True

# WITH
def with_sieve(k):
    i = 2
    while i * i <= k:
        if k % i != 0:
            print(i)

        # DO WHILE
        while True:
            i += 1
            if is_prime(i):
                break


# WITHOUT
def without(k):
    i = 2
    while i <= k:
        if is_prime(i):
            print(i)
        i += 1



if __name__ == "__main__":
    use_sieve = input("Use the sieve? (y/N) ")
    print(use_sieve)
    k = int(input("Insert k: "))
    if use_sieve.lower() in ['true', '1', 't', 'y', 'yes']:
        with_sieve(k)
    else:
        without(k)
