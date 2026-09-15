"""Prime number helpers.

This is the code we built up in class, ending at the version from slide 17.
"""


def is_prime(number):
    """Return True if `number` is prime."""
    if number <= 1:
        return False
    for element in range(2, number):
        if number % element == 0:
            return False
    return True


def print_next_prime(number):
    """Print the first prime strictly greater than `number`."""
    index = number
    while True:
        index += 1
        if is_prime(index):
            print(index)
            return index


if __name__ == "__main__":
    print_next_prime(10)
