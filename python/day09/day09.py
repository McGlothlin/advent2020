from common import readList
from collections import deque
from itertools import combinations, starmap

class XmasCypher:
    def __init__(self, max_length: int, filename='input.txt'):
        self.input_list = readList(filename, int)
        self.max_length = max_length

        self.input_deque = deque(self.input_list[0:self.max_length], maxlen=self.max_length)
        self.target_index = 0

    def part1(self):
        for i in range(self.max_length, len(self.input_list)):
            next_value = self.input_list[i]

            if not any(starmap(lambda x, y: x + y == next_value, combinations(self.input_deque, 2))):
                self.target_index = i
                return next_value

            self.input_deque.popleft()
            self.input_deque.append(next_value)

        return None


    def getContiguousElements(self):
        buffer_size = self.max_length
        sequences = []

        i = 0
        while i <= self.target_index:
            buffer = []
            j = i
            while (j - i) <= buffer_size and j <= self.target_index:
                buffer.append(self.input_list[j])
                # Sum at least two numbers.
                if len(buffer) > 1:
                    sequences.append(list(buffer))
                j += 1
            i += 1

        return sequences


    def part2(self):
        target = self.input_list[self.target_index]
        sequences = self.getContiguousElements()

        for sequence in sequences:
            if sum(sequence) == target and len(sequence) > 1:
                return sum([max(sequence), min(sequence)])

        return None




def main():
    cypher = XmasCypher(25)
    part1 = cypher.part1()
    part2 = cypher.part2()

    print(f'Answer 1: {part1}')
    print(f'Answer 2: {part2}')


if __name__ == '__main__':
    main()
