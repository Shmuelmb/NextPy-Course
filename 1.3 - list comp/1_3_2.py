def is_prime(number):
    result = [i for i in range(1, number + 1) if number % i == 0]
    return len(result) == 2


# print(is_prime(178))  # normal number
# print(is_prime(191))  # prime number
