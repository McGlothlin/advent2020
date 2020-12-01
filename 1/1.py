from typing import Optional
from common import readList

def get2020Product() -> Optional[int]:
    expense_list = readList('input.txt', int)
    for multiplicand in expense_list:
        for multiplier in expense_list:
            if multiplicand + multiplier == 2020:
                return multiplicand * multiplier
    return None


def get2020ProductPart2() -> Optional[int]:
    expense_list = readList('input.txt', int)
    for first in expense_list:
        for second in expense_list:
            for third in expense_list:
                if first + second + third == 2020:
                    return first * second * third
    return None


def main():
    answer = get2020Product()
    answer = get2020ProductPart2()
    print(f'Answer: {answer}')


if __name__ == '__main__':
    main()
