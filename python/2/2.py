from common import readList

def answerTwo():
    valid = []
    for line in readList('input.txt'):
        occurrences, character, password = line.split(' ')
        occurrences = list(map(lambda x: int(x)-1, occurrences.split('-')))
        character = character.strip(':')
        assert(len(occurrences) == 2)

        if bool(password[occurrences[0]] == character) ^ bool(password[occurrences[1]] == character):
            valid.append(line)

    return len(valid)


def main():
    # I did this not because it's good code, but to see if I could make it work. It works.
    # I wanted to use `range(*map(int, occurrences.split('-')))` on the first line but the max of range() is exclusive.
    part1 = [int(occurrences.split('-')[0]) <= password.count(character.strip(':')) <= int(occurrences.split('-')[-1])
             for occurrences, character, password in [line.split(' ') for line in readList('input.txt')]].count(True)

    part2 = answerTwo()

    print(f'Answer 1: {part1}')
    print(f'Answer 2: {part2}')


if __name__ == '__main__':
    main()
