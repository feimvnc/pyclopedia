"""Various validators"""


def validate_integer(
    arg_name, arg_value, min_value = None, max_value = None, 
    custom_min_message=None, custom_max_message=None
):
    """Validates an integer

    Args:
        arg_name (str): the name of the argument
        arg_value (obj): the value being validated
        min_value (int, optional): specifies the min value. Defaults to None.
        max_value (int, optional): specifies the max value. Defaults to None.
        custom_min_message (_type_, optional): custom message when value is less than minimum. Defaults to None.
        custom_max_message (_type_, optional): custom message when value is greater than maximum. Defaults to None.

    Returns:  
        None: no exception raised if validdation passes

    Raises: 
        TypeError: if 'arg_value' is not an integer 
        ValueError: if 'arg_value' does not satisfy the bounds
    """

    if not isinstance(arg_value, int):
        raise TypeError(f'{arg_name} must be an integer.')

    if min_value is not None and arg_value < min_value:
        if custom_min_message is not None:
            raise ValueError(custom_min_message)
        raise ValueError(f'{arg_name} cannot be less than {min_value}')

    if max_value is not None and arg_value > max_value:
        if custom_max_message is not None:
            raise ValueError(custom_max_message)
        raise ValueError(f'{arg_name} cannot be greater than {max_value}')
        