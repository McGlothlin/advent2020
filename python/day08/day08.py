from common import readList
import re

class AsmReader:
    def __init__(self, boot_check, filename='input.txt'):
        self.accumulator = 0
        self.instructions = readList(filename=filename)
        self.instructions_read = set()
        self.boot_check = boot_check

        self.instruction_pattern = re.compile(r'^(acc|jmp|nop) ([+\-])(\d+)$')

    def execute(self):
        # for i in range(0, len(self.instructions)):
        i = 0
        while i < len(self.instructions):
            instruction = re.findall(self.instruction_pattern, self.instructions[i]).pop()
            if i in self.instructions_read:
                # About to re-read an instruction. Exit for part 1.
                if self.boot_check:
                    raise ArithmeticError(f'Infinite loop! Repeated line {i}.')
                return self.accumulator
            self.instructions_read.add(i)

            if len(instruction) == 1:
                # noop
                continue
            command, direction, magnitude = instruction
            magnitude = int(magnitude)
            if command == 'acc':
                if direction == '+':
                    self.accumulator += magnitude
                elif direction == '-':
                    self.accumulator -= magnitude
                else:
                    raise ValueError(f'Unexpected instruction: {self.instructions[i]}')
            elif command == 'jmp':
                if direction == '+':
                    i += magnitude
                elif direction == '-':
                    i -= magnitude
                else:
                    raise ValueError(f'Unexpected instruction: {self.instructions[i]}')
                # Do not increment i for the jmp command.
                continue

            i += 1
        if i == len(self.instructions):
            print('Execution halted.')
            return self.accumulator
        print('Execution halted.')


def main():
    reader = AsmReader()
    part1 = reader.execute()

    # part2 = bag_builder.getBagCount('shiny gold')
    #
    print(f'Answer 1: {part1}')
    # print(f'Answer 2: {part2}')

if __name__ == '__main__':
    main()