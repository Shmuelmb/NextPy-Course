
def sum_digit_number(num: int):
    """
    Calculates the sum of the digits of a given number.

    Args:
        num (int): The number whose digits need to be summed.

    Returns:
        int: The sum of the digits of the given number.

    Example:
        sum_digit_number(12)  # Returns 3
    """
    if num <= 9:
        return num
    else:
        return sum([int(i) for i in str(num)])


def check_id_valid(id_number: int):
    """
    Check if the given ID number is valid.

    Args:
        id_number (int): The ID number to be checked.

    Returns:
        bool: True if the ID number is valid, False otherwise.
    """
    id_number = str(id_number)
    # Multiply even digit by 2
    multiply_list = [int(id_number[num]) if num % 2 == 0 else int(
        id_number[num]) * 2 for num in range(0, len(id_number))]
    # Sum the digits
    result = sum([sum_digit_number(num) for num in multiply_list])
    return result % 10 == 0


def id_generator(id_number: int):
    """
    Generate a sequence of ID numbers starting from the given ID number.

    Args:
        id_number (int): The starting ID number.

    Yields:
        int: The next valid ID number in the sequence.

    """
    while id_number < 999999999:
        if check_id_valid(id_number):
            yield id_number
        id_number += 1


class IDIterator():
    """
     A class used to generate a sequence of ID numbers
        starting from the given ID number.
    """

    def __init__(self, id: int):
        """Initialize the IDIterator

        Args:
            _id (int): The starting ID number
        """
        self._id = id

    def __iter__(self):
        return self

    def __next__(self):
        """
        Generates the next valid ID in a sequence.

        Returns:
            int: The next valid ID in the sequence.

        Raises:
            StopIteration: If the maximum ID value has been reached.
        """
        while self._id < 999999999:
            self._id += 1  # Increment the ID unconditionally in each iteration
            if check_id_valid(self._id):
                return self._id
        raise StopIteration


def main():
    user_id = int(input("Enter your ID: "))
    user_choose = (input("Generator or Iterator? (gen/it)?: "))
    if user_choose == "it":
        iter_id_pull = IDIterator(user_id)
        for _ in range(1, 11):
            # Print the next ID in the sequence
            print(next(iter_id_pull))

    elif user_choose == "gen":
        try:
            generator_id_pull = id_generator(user_id)
            for _ in range(1, 11):
                # Print the next ID in the sequence
                print(next(generator_id_pull))
        except StopIteration:
            print("StopIteration: The maximum ID value has been reached.")


if __name__ == "__main__":
    main()
