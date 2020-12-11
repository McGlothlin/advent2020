import collections
from common import readList, inclusiveRange

class DaisyChain:
    def __init__(self, filename='input.txt'):
        self.input_list = [0] + readList(filename, int)
        self.list_combinations = set()


    def part1(self, min_jolt_delta, max_jolt_delta, initial_jolt=0, builtin_adapter_offset=3, skip_range=range(0)):
        self.input_list.sort()
        current_joltage = 0
        # Counts the occurrence of each delta. Add one so our list indices will match the deltas.
        difference_counter = [0] * (max_jolt_delta + 1)

        new_list = []

        for i in range(0, len(self.input_list)):
            if i in skip_range:
                continue
            adapter = self.input_list[i]
            joltage_delta = adapter - current_joltage
            if joltage_delta in inclusiveRange(min_jolt_delta, max_jolt_delta):
                difference_counter[joltage_delta] += 1
                current_joltage += joltage_delta

                new_list.append(adapter)
            else:
                return None

        if min_jolt_delta == initial_jolt:
            difference_counter[min_jolt_delta] += 1
        if max_jolt_delta == builtin_adapter_offset:
            difference_counter[max_jolt_delta] += 1

        self.list_combinations.add(tuple(new_list))
        return difference_counter[min_jolt_delta] * difference_counter[max_jolt_delta]


    # def part2(self, start_index=0, stop_index=0, valid_chains=0):
    #     self.input_list.sort()
    #
    #     # Base case
    #     if stop_index > len(self.input_list):
    #         return valid_chains
    #
    #     if self.part1(min_jolt_delta=1, max_jolt_delta=3, initial_jolt=0, builtin_adapter_offset=3,
    #                   skip_range=range(start_index, stop_index)):
    #         valid_chains += 1
    #         stop_index += 1
    #     else:
    #         start_index += 1
    #         stop_index = start_index + 1
    #
    #     return self.part2(start_index, stop_index, valid_chains)


    # This is the result of me looking it up. I'm not even sorry.
    # Explanation preserved here
    # https://www.reddit.com/r/adventofcode/comments/ka8z8x/2020_day_10_solutions/gfbo61q?utm_source=share&utm_medium=web2x&context=3
    #
    # Logic: count all possible input paths into an adapter / node, start from wall,
    # propagate the count up till the end of chain.
    #
    # - start from wall adapter (root node) with input count 1
    # - add this count to the next 1, 2 or 3 adapters / nodes
    # - add their input counts to next adapters / nodes
    # - repeat this for all adapters (in sorted order)
    # - you'll end up with input count for your device adapter
    def part2(self):
        counter = collections.Counter({0: 1})
        self.input_list.sort()
        foo = self.input_list[-1] + 3
        self.input_list.append(foo)

        for entry in self.input_list:
            counter[entry + 1] += counter[entry]
            counter[entry + 2] += counter[entry]
            counter[entry + 3] += counter[entry]

        return counter[max(self.input_list)]


def main():
    chain = DaisyChain()
    part1 = chain.part1(min_jolt_delta=1, max_jolt_delta=3, initial_jolt=0, builtin_adapter_offset=3)
    part2 = chain.part2()

    print(f'Answer 1: {part1}')
    print(f'Answer 2: {part2}')


if __name__ == '__main__':
    main()
