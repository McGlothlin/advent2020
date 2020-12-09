from common import readList
from collections import deque
from itertools import combinations, starmap

class XmasCypher:
    def __init__(self, max_length: int, filename='input.txt'):
        self.input_list = readList(filename, int)
        self.input_deque = deque(self.input_list, maxlen=max_length)
        self.max_length = max_length

    def part1(self):
        input_deque = deque(self.input_list[0:self.max_length], maxlen=self.max_length)
        for i in range(self.max_length, len(self.input_list)):
            next_value = self.input_list[i]

            if not any(starmap(lambda x, y: x + y == next_value, combinations(input_deque, 2))):
                return next_value

            input_deque.popleft()
            input_deque.append(next_value)


def main():
    cypher = XmasCypher(25)
    part1 = cypher.part1()
    # part2 = reader.bootCheck()

    print(f'Answer 1: {part1}')
    # print(f'Answer 2: {part2}')


if __name__ == '__main__':
    main()