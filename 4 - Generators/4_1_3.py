def is_prime(number):
    result = any([number % i == 0 for i in range(2, number)]) == False
    return result


def prime_generator(n):
    while True:
        if is_prime(n):
            yield n
        n += 1


def first_prime_over(n):
    return next(prime_generator(n))


def main():
    print(first_prime_over(24))


if __name__ == '__main__':
    main()
