from common import readList
import re

class AsmReader:
    def __init__(self, filename='input.txt'):
        self.accumulator = 0
        self.instructions = readList(filename=filename)
        self.instructions_read = set()

        self.instruction_pattern = re.compile(r'^(acc|jmp|nop) ([+\-])(\d+)$')

    def execute(self, boot_check=False):
        i = 0
        while i < len(self.instructions):
            instruction = re.findall(self.instruction_pattern, self.instructions[i]).pop()
            if i in self.instructions_read:
                # About to re-read an instruction. Exit for part 1.
                if boot_check:
                    raise ArithmeticError(f'Infinite loop! Repeated line {i}.')
                else:
                    return self.accumulator
            self.instructions_read.add(i)

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
        return self.accumulator


    def bootCheck(self):
        acc = None
        self.accumulator = 0
        self.instructions_read = set()

        for i in range(0, len(self.instructions)):
            if self.instructions[i].startswith('jmp'):
                old_line = self.instructions[i]
                self.instructions[i] = self.instructions[i].replace('jmp', 'nop')
            elif self.instructions[i].startswith('nop'):
                old_line = self.instructions[i]
                self.instructions[i] = self.instructions[i].replace('nop', 'jmp')
            else:
                continue

            try:
                acc = self.execute(boot_check=True)
                break
            except ArithmeticError:
                # Revert our changes.
                self.accumulator = 0
                self.instructions_read = set()
                self.instructions[i] = old_line
                continue
        return acc


def main():
    reader = AsmReader()
    part1 = reader.execute()
    part2 = reader.bootCheck()

    print(f'Answer 1: {part1}')
    print(f'Answer 2: {part2}')


if __name__ == '__main__':
    main()