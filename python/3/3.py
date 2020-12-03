from common import readList

def treesHit(right: int, down: int) -> int:
    tree_map = readList()
    trees_hit = 0

    row_num = 0
    width_increment = right

    for line in tree_map:
        if row_num % down != 0:
            row_num += 1
            continue

        # The pattern repeats
        col_num = (row_num * width_increment) % len(line)

        if line[col_num] == '#':
            trees_hit += 1

        row_num += 1

    return trees_hit


def main():
    part1 = treesHit(3, 1)
    part2 = treesHit(1, 1) * treesHit(3, 1) * treesHit(5, 1) * treesHit(7, 1) * treesHit(1, 2)

    print(f'Answer 1: {part1}')
    print(f'Answer 2: {part2}')


if __name__ == '__main__':
    main()
