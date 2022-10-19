def is_prime(n):
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True

if __name__ == "__main__":
    k = int(input("Insert k (>=2)"))
    print(is_prime(k))