import re
from typing import Any, List

STD_OBJ_SEPARATOR = re.compile('\n{2}')

def splitObjects(input_str: str) -> List[str]:
    return re.split(STD_OBJ_SEPARATOR, input_str)


def readList(filename: str = './input.txt', func = str) -> Any:
    """ Reads a file and returns a list of type `func`.

        Raises a TypeError if `func` is not a unary type conversion function.
    """
    with open(filename, 'r') as f:
        input_list = f.readlines()
        try:
            if func == str:
                return [func(x).strip() for x in input_list]
            return [func(x) for x in input_list]
        except TypeError as e:
            print(f'Error: type {func} not allowed here.')
            raise e


def readString(filename: str = './input.txt') -> str:
    with open(filename, 'r') as f:
        return f.read()


def inclusiveRange(start: int, stop: int) -> range:
    return range(start, stop + 1)
