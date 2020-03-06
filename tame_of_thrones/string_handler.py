"""The string handler module."""


class StringHandlerError(BaseException):
    pass


class InsufficientDataError(StringHandlerError):
    pass


class InvalidInputError(StringHandlerError):
    pass


def is_string(input_str):
    """To know if a value of list of all values is of stype str.

        Args:
            input_str(str or list of strings): input value

        Returns:
        bool: True if the values are of type string.

    """
    if not isinstance(input_str, list):
        input_str = [input_str]

    for value in input_str:
        if not isinstance(value, str):
            return False
    return True

def char_counter(input_str):
    """Counts the chars of a string.

        Args:
            input_str(string): input string

        Retuns:
            dict: Dictionary of characters as keys and their number of occurences as values.
                Example: "geek" -> {'g':1, 'e':2, 'k':1}

    """
    if not is_string(input_str):
        raise InvalidInputError

    count = {}
    for char in input_str:
        count[char] = count[char] + 1 if count.get(char, None) else 1
    return count

def contains_sub_str_letters(main_str=None, sub_str=None):
    """Returns true of all characters of substring are in main string.

        Args:
            main_str(string): The main string
            sub_str(string): The sub string

        Returns:
            bool: True if all characters of sub string are in main string (occurences inclusive)
                False if not.

    """
    if not main_str and sub_str:
        raise InsufficientDataError

    if not is_string([main_str, sub_str]):
        raise InvalidInputError
    if len(main_str) < len(sub_str):
        return False
    main_str_counter = char_counter(main_str)
    sub_str_counter = char_counter(sub_str)
    for char in sub_str:
        if sub_str_counter[char] > main_str_counter.get(char, 0):
            return False
    return True
