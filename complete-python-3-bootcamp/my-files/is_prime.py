import math

# Function that checks return True if number is prime and False if not


def is_prime(number):
    if number % 2 == 0 and number > 2:
        return False
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True


if __name__ == '__main__':
    print(is_prime(5))
