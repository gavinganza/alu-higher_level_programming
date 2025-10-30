#!/usr/bin/python3
"""
4-list_division.py
A function that safely divides elements from two lists up to a specified
length,
handling TypeErrors, ZeroDivisionErrors, and IndexErrors.
"""


def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element two lists.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of divisions to attempt.

    Returns:
        list: A new list of length list_length with the division results,
              or 0 (integer) if an error occurred for that element.
    """
    new_list = []

    # Iterate up to the specified list_length
    for i in range(list_length):
        # Initialize result to integer 0, required for error cases.
        result = 0

        try:
            # Attempt to access elements and perform division
            num1 = my_list_1[i]
            num2 = my_list_2[i]

            # Python 3 division (/) always returns a float
            result = num1 / num2

        except ZeroDivisionError:
            # Handle division by zero
            print("division by 0")
            result = 0  # Set result to integer 0

        except TypeError:
            # Handle non-numeric types
            print("wrong type")
            result = 0  # Set result to integer 0

        except IndexError:
            # Handle list shorter than list_length
            print("out of range")
            result = 0  # Set result to integer 0

        finally:
            # This block executes regardless of whether an exception occurred.
            new_list.append(result)

    return new_list
