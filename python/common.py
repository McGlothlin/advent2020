def readList(filename: str, func=str):
    """ Reads a file and returns a list of floats. """
    with open(filename, 'r') as f:
        input_list = f.readlines()
        try:
            if func == str:
                return [func(x).strip() for x in input_list]
            return [func(x) for x in input_list]
        except TypeError as e:
            print(f'Error: type {func} not allowed here.')
            raise e
