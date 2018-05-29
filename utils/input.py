import sys

from clint.textui import puts, colored


def query_yes_no(question):
    """
    Ask a yes/no question via raw_input() and return their answer
    Args:
        question: str
            that is presented to the user
    Returns:
        result: bool
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    while True:
        puts("{0} (y/n):".format(question))
        choice = input().strip().lower()
        if choice in valid:
            return valid.get(choice)
        else:
            puts(colored.red("Please respond with 'yes' or 'no' (or 'y' or 'n')."))


def _validate_input(input_type, valid_choice):
    """
        validate input type
    Args:
        input_type: int or str or float
        valid_choice: dict or list

    Returns:
        None. no exception is OK
    """
    if input_type not in [int, str, float]:
        raise TypeError("input_type must in (int, str, float). your type is {0}".format(input_type.__name__))

    if valid_choice is not None:
        if not isinstance(valid_choice, (list, dict)):
            raise TypeError("valid_choice must in (list, dict)")

        if not valid_choice:
            raise ValueError("valid_choice can't be null!")

        t = valid_choice if isinstance(valid_choice, list) else valid_choice.keys()
        if not all(isinstance(x, input_type) for x in t):
            raise TypeError("valid_choice element type must be {0}".format(input_type.__name__))


def _print_choice(valid_choice, print_choice=True):
    """

    Args:
        valid_choice: list or dict
        print_choice: bool

    Returns:

    """
    if print_choice and valid_choice:
        if isinstance(valid_choice, dict):
            for key, value in valid_choice.iteritems():
                puts("{0}. {1}".format(colored.green(str(key)), value))
        elif isinstance(valid_choice, list):
            for i in valid_choice:
                puts(colored.green(str(i)))


def choice(question, input_type=int, default_value=None, valid_choice=None, print_choice=True):
    """
        get some value by input
    Args:
        question: str
            that is presented to the user
        input_type: int or str or float
            input type
        default_value: int or float
            input is none will return this. use this arg valid_choice must be null
            input_type must be int
        valid_choice: dict or list
        print_choice: bool
            valid_choice not null will print the choice
    Returns:
        if valid_choice is not null will get value from valid_choice.
        if valid_choice is null return your input
    Raises:
        TypeError:
            input_type must in [int, str]
            valid_choice type must in [list, dict]
            valid_choice key type must same as input_type
        ValueError:
            valid_choice can't be {} or []
    """

    _validate_input(input_type, valid_choice)

    if default_value:
        if not isinstance(default_value, input_type) or input_type not in [int, float]:
            raise TypeError("input_type must in (int, float) and {0} must match {1}".format(default_value, input_type))
    while True:
        puts(question)
        _print_choice(valid_choice, print_choice)
        sys.stdout.write("choice:" if valid_choice else "input:")
        choice = input().strip()
        if choice == '' and default_value:
            return default_value
        if input_type in (float, int):
            try:
                choice = int(choice) if input_type == int else float(choice)
            except ValueError:
                puts(colored.red("Please enter a valid number."))
                continue
        if valid_choice and choice in valid_choice:
            return valid_choice.get(choice) if isinstance(valid_choice, dict) else choice
        elif valid_choice is None and choice:
            return choice
        puts(colored.red("Select invalid Please reselect."))


def multiple_choice(question, input_type=int, valid_choice=None, print_choice=True):
    """
        multiple choice input.
    Args:
        question: str
            that is presented to the user
        input_type: int or str
        valid_choice: dict or list
        print_choice: bool
            valid_choice not null will print the choice
    Returns:
        result: list
    Raises:
        TypeError:
            input_type must in [int, str]
            valid_choice type must in [list, dict]
            valid_choice key type must same as input_type
        ValueError:
            valid_choice can't be {} or []
    """

    def invalid_input():
        puts(colored.red("Select invalid Please reselect."))

    _validate_input(input_type, valid_choice)

    while True:
        puts(question)
        _print_choice(valid_choice, print_choice)
        sys.stdout.write("choices (separate by commas if necessary):")
        try:
            choices = [int(c.strip()) for c in input().split(",")]
        except ValueError:
            puts(colored.red("Please enter a valid number."))
            continue
        if valid_choice is None and choices:
            return choices
        elif valid_choice and choices:
            if [c for c in choices if c not in valid_choice]:
                invalid_input()
                continue
            if isinstance(valid_choice, dict):
                return [valid_choice.get(c) for c in choices]
            return list(set(choices))


def input_in_range(question, start, end, input_type=int, default_value=None):
    """

    Args:
        question: str
            that is presented to the user
        start: int or float
            type must match input_type. the start range
        end: int or float
            type must match input_type. the end range
        input_type: int or float
        default_value: int or float
            type must match input_type
    Returns:
        input value
    """
    if input_type not in [int, float]:
        raise TypeError("input_type must in [int, float]. not be {0}".format(input_type))
    if not isinstance(start, input_type) or not isinstance(end, input_type):
        raise TypeError("start and end type must be {0}".format(input_type))
    if default_value and not isinstance(default_value, input_type):
        raise TypeError("default_value type must be {0}".format(input_type))
    if start >= end:
        raise ValueError("start({0}) must less than end({1}).".format(start, end))
    if default_value and not start <= default_value <= end:
        raise ValueError("default value({0}) required: {1} <= val <= {2}".format(default_value, start, end))

    while True:
        i = choice(question=question, input_type=input_type, default_value=default_value)
        if start <= i <= end:
            return i
        have_default = "default:{0}".format(default_value) if default_value else ''
        puts(colored.red("Please enter a valid number (required: {0} <= val <= {1} {2}).".
                         format(start, end, have_default)))
