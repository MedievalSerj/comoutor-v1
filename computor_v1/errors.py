

class InputError(ValueError):

    def __init__(self, message='Invalid argument'):
        super().__init__(message)
