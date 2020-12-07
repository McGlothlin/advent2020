import itertools
from typing import List
from common import readList

def getRow(boarding_pass: str, total_rows):
    row = 0
    increment = total_rows
    for i in range(0, 7):
        increment //= 2
        if boarding_pass[i] == 'B':
            row += increment
    return row


def getCol(boarding_pass: str, total_cols: int):
    col = 0
    increment = total_cols
    for i in range(7, 10):
        increment //= 2
        if boarding_pass[i] == 'R':
            col += increment
    return col


def getSeatID(row, col):
    return row * 8 + col


def getSeatIDs():
    seat_ids: List[int] = []
    max_row = 128
    max_col = 8
    for boarding_pass in readList():
        row, col = getRow(boarding_pass, max_row), getCol(boarding_pass, max_col)
        seat_id = getSeatID(row, col)
        seat_ids.append(seat_id)

    return seat_ids


def getMaxSeatID():
    return max(getSeatIDs())


def getMissingSeatID():
    max_row = 128
    max_col = 8
    all_seats = itertools.product(range(max_row), range(max_col))
    filled_seat_ids = getSeatIDs()
    for row, col in all_seats:
        seat_id = getSeatID(row, col)
        if seat_id not in filled_seat_ids:
            # Check for adjacent seats. They should be filled.
            if (seat_id + 1) not in filled_seat_ids or (seat_id - 1) not in filled_seat_ids:
                continue

            return seat_id
    return None


def main():

    part1 = getMaxSeatID()
    part2 = getMissingSeatID()

    print(f'Answer 1: {part1}')
    print(f'Answer 2: {part2}')


if __name__ == '__main__':
    main()
