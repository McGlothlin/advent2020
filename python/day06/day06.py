from common import splitObjects, readString

def getGroups():
    return splitObjects(readString())


def getDistinctYesAnswers(groups):
    yes_answers = [set(group.replace('\n', '')) for group in groups]
    sum_of_yes = sum([len(x) for x in yes_answers])
    return sum_of_yes


def getAllYesAnswers(groups):
    group_totals = []
    for group in groups:
        # Counts the number of yeses per group
        yes_counter: dict = {}
        num_persons: int = 0
        for person in group.split('\n'):
            num_persons += 1
            for answer in list(person):
                if answer not in yes_counter:
                    yes_counter[answer] = 1
                else:
                    yes_counter[answer] += 1

        all_answered = 0
        for answer, count in yes_counter.items():
            if count == num_persons:
                all_answered += 1
        group_totals.append(all_answered)

    return sum(group_totals)


def main():

    part1 = getDistinctYesAnswers(getGroups())
    part2 = getAllYesAnswers(getGroups())

    print(f'Answer 1: {part1}')
    print(f'Answer 2: {part2}')


if __name__ == '__main__':
    main()
