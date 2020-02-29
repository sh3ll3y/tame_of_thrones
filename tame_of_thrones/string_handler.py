"""The string handler module."""

class StringHandlerError(BaseException):
    pass

class InsufficientDataError(StringHandlerError):
    pass 

class InvalidInputError(StringHandlerError):
    pass 

def is_string(input_str):

    if not isinstance(input_str, list):
        input_str = [input_str]
    
    for value in input_str:
        if not isinstance(value, str):
            return False
    return True


def char_counter(input_str):
    if not is_string(input_str):
        raise InvalidInputError

    count = {}
    for char in input_str:
        count[char] = count[char] + 1 if count.get(char, None) else 1
    return count

def contains_sub_str_letters(main_str=None, sub_str=None):
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