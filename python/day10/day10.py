from common import readList, inclusiveRange

class DaisyChain:
    def __init__(self, filename='input.txt'):
        self.input_list = readList(filename, int)


    def part1(self, min_jolt_delta, max_jolt_delta, initial_jolt=0, builtin_adapter_offset=3):
        self.input_list.sort()
        current_joltage = 0
        # Counts the occurrence of each delta. Add one so our list indices will match the deltas.
        difference_counter = [0] * (max_jolt_delta + 1)

        for adapter in self.input_list:
            joltage_delta = adapter - current_joltage
            if joltage_delta in inclusiveRange(min_jolt_delta, max_jolt_delta):
                difference_counter[joltage_delta] += 1
                current_joltage += joltage_delta

        if min_jolt_delta == initial_jolt:
            difference_counter[min_jolt_delta] += 1
        if max_jolt_delta == builtin_adapter_offset:
            difference_counter[max_jolt_delta] += 1

        return difference_counter[min_jolt_delta] * difference_counter[max_jolt_delta]


def main():
    chain = DaisyChain()
    part1 = chain.part1(min_jolt_delta=1, max_jolt_delta=3, initial_jolt=0, builtin_adapter_offset=3)
    # part2 = cypher.part2()

    print(f'Answer 1: {part1}')
    # print(f'Answer 2: {part2}')


if __name__ == '__main__':
    main()
