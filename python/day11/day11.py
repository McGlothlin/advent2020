from typing import List
from copy import deepcopy


def read_matrix(filename: str) -> List[List[str]]:
    with open(filename, 'r') as f:
        matrix = [list(row) for row in f.read().splitlines()]

    return matrix


# Part 1
# List of occupied status, starting with top left corner adjacent seat (diagonals included)
def get_adjacent_seat_status(seats: List[List[str]], x: int, y: int) -> List[str]:
    combinations_x: List[int] = [x+1, x, x-1]
    combinations_y: List[int] = [y+1, y, y-1]
    adjacent_seats = []
    for i in combinations_x:
        for j in combinations_y:
            try:
                # Conditions where we don't want to include an adjacent value.
                if i < 0 or j < 0:
                    continue
                if i == x and j == y:
                    continue
                adjacent_seats.append(seats[i][j])
            except IndexError:
                # Out of bounds
                pass
    return adjacent_seats


# Part 2 ###############################################################################################################
# Not terribly happy with this solution but it works and is the first thing I thought of.
# It is very slow with the full input set.
def check_direction(x, y, seats, visible_seats, seat_encountered):

    if seat_encountered:
        return True

    while True:
        try:
            if x < 0 or y < 0 or seats[x][y] == '.':
                break
            if seats[x][y] == 'L' or seats[x][y] == '#':
                visible_seats.append(seats[x][y])
                seat_encountered = True
                break
        except IndexError:
            # Out of bounds
            break

    return seat_encountered


# Includes all visible spaces in each of the eight cardinal and ordinal directions (diagonals included)
def get_visible_seat_status(seats: List[List[str]], x: int, y: int) -> List[str]:
    visible_seats = []
    # Counter for our movements
    n = 1

    # Halts the loop in check_direction() when a seat is already encountered.
    # We can't see through a seat, whether occupied or not.
    seat_encountered_e = False
    seat_encountered_se = False
    seat_encountered_s = False
    seat_encountered_sw = False
    seat_encountered_w = False
    seat_encountered_nw = False
    seat_encountered_n = False
    seat_encountered_ne = False

    while n < len(seats):
        # E
        seat_encountered_e = check_direction(x+n, y, seats, visible_seats, seat_encountered_e)
        # SE
        seat_encountered_se = check_direction(x+n, y+n, seats, visible_seats, seat_encountered_se)
        # S
        seat_encountered_s = check_direction(x, y+n, seats, visible_seats, seat_encountered_s)
        # SW
        seat_encountered_sw = check_direction(x-n, y+n, seats, visible_seats, seat_encountered_sw)
        # W
        seat_encountered_w = check_direction(x-n, y, seats, visible_seats, seat_encountered_w)
        # NW
        seat_encountered_nw = check_direction(x-n, y-n, seats, visible_seats, seat_encountered_nw)
        # N
        seat_encountered_n = check_direction(x, y-n, seats, visible_seats, seat_encountered_n)
        # NE
        seat_encountered_ne = check_direction(x+n, y-n, seats, visible_seats, seat_encountered_ne)

        n += 1

    return visible_seats
# End Part 2 ###########################################################################################################


# Determines whether a seat change is needed.
def change_seat(original_seat: str, adjacent_list: List[str], updated_seats: List[List[str]], i: int, j: int
                , occupied_seat_count):

    # How many seats can be occupied before somebody moves.
    tolerance: int = 5

    # Check our rules
    if original_seat == 'L' and '#' not in adjacent_list:
        updated_seats[i][j] = '#'
        occupied_seat_count += 1
    elif original_seat == '#' and adjacent_list.count('#') >= tolerance:
        updated_seats[i][j] = 'L'
        occupied_seat_count -= 1
    else:
        updated_seats[i][j] = original_seat

    return occupied_seat_count


def write_matrix(matrix, outfile):
    with open(outfile, 'w') as f:
        f.writelines([''.join(row) + '\n' for row in matrix])


def main():
    input_filename = 'input.txt'
    current_occupied_seat_count = 0
    previous_occupied_seat_count = -1
    number_of_rounds = 0
    original_seats = read_matrix(input_filename)

    # None of that shallow copy nonsense here
    updated_seats = read_matrix(input_filename)

    while True:
        max_x = len(original_seats)
        max_y = len(original_seats[0])
        for i in range(0, max_x):
            for j in range(0, max_y):
                #################################################################
                # Toggle for Part 1
                # adjacent_list = get_adjacent_seat_status(original_seats, i, j)
                #################################################################
                # Toggle for Part 2
                adjacent_list = get_visible_seat_status(original_seats, i, j)
                #################################################################
                current_occupied_seat_count = change_seat(original_seats[i][j], adjacent_list, updated_seats, i, j,
                                                          current_occupied_seat_count)
        number_of_rounds += 1
        if current_occupied_seat_count == previous_occupied_seat_count:
            break
        original_seats = deepcopy(updated_seats)
        previous_occupied_seat_count = current_occupied_seat_count
        write_matrix(updated_seats, 'output.txt')
        print('Round ' + str(number_of_rounds) + ' complete.')


    write_matrix(updated_seats, 'output.txt')
    print('Number of occupied seats: ' + str(current_occupied_seat_count))


if __name__ == '__main__':
    main()
