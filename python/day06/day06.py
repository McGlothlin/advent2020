from common import splitObjects, readString

def getGroups():
    return splitObjects(readString())


def getYesAnswers(groups):
    yes_answers = [set(x.replace('\n', '')) for x in groups]
    sum_of_yes = sum([len(x) for x in yes_answers])
    return sum_of_yes


def main():

    part1 = getYesAnswers(getGroups())
    # part2 = getMissingSeatID()

    print(f'Answer 1: {part1}')
    # print(f'Answer 2: {part2}')


if __name__ == '__main__':
    main()
