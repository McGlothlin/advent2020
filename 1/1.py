from typing import Optional
from common import readList

def get2020Product() -> Optional[int]:
    expense_list = readList('input.txt', int)
    for multiplicand in expense_list:
        for multiplier in expense_list:
            if multiplicand + multiplier == 2020:
                return multiplicand * multiplier
    return None


def main():
    answer = get2020Product()
    print(f'Answer: {answer}')


if __name__ == '__main__':
    main()
