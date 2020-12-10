from common import readList, inclusiveRange

class DaisyChain:
    def __init__(self, filename='input.txt'):
        self.input_list = readList(filename, int)
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


    def part2(self, start_index=0, stop_index=0, valid_chains=0):
        self.input_list.sort()

        # Base case
        if stop_index > len(self.input_list):
            return valid_chains

        if self.part1(min_jolt_delta=1, max_jolt_delta=3, initial_jolt=0, builtin_adapter_offset=3,
                      skip_range=range(start_index, stop_index)):
            valid_chains += 1
            stop_index += 1
        else:
            start_index += 1
            stop_index = start_index + 1

        # Tail recursion
        valid_chains += self.part2(start_index, stop_index, valid_chains)

        return valid_chains

def main():
    chain = DaisyChain()
    part1 = chain.part1(min_jolt_delta=1, max_jolt_delta=3, initial_jolt=0, builtin_adapter_offset=3)
    # part2 = cypher.part2()

    print(f'Answer 1: {part1}')
    # print(f'Answer 2: {part2}')


if __name__ == '__main__':
    main()
