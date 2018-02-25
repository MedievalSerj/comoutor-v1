

class InputError(ValueError):

    def __init__(self, message='Invalid argument'):
        super(InputError, self).__init__(message)


def format_error(error_msg, *args):
    msg = 'computor: ' + error_msg
    for item in args:
        msg += '\n' + item
    return msg


def format_position_indicator(error_indices, size):
    msg = ' ' * size
    for i in error_indices:
        msg = msg[:i] + '^' + msg[i+1:]
    return msg


def create_error(error_msg, error_index, equation_str):
    return format_error(
        error_msg,
        equation_str,
        format_position_indicator(error_index, len(equation_str))
    )
