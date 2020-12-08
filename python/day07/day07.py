import re
from common import readList

class BagBuilder:
    def __init__(self, filename: str = 'input.txt'):
        self.input_list = readList(filename=filename)
        # A list of top level bags found at the start of each line
        self.bag_graph = {}
        self.gold_list = []
        self.total_bags: int = 0

    # Simple tokenizer using space ' ' as the token separator.
    def buildGraph(self):
        bag_definition = re.compile(r'^(\w+ \w+) bag')
        bag_contents = re.compile(r'(\d+ \w+ \w+) bag')

        for line in self.input_list:
            # Split match on spaces, initialize new top level bag. There should only be one top level bag match.
            bag = re.search(bag_definition, line).group(1)

            if bag not in self.bag_graph:
                self.bag_graph[bag] = {}

            for nested_bag in re.findall(bag_contents, line):
                nested_bag_tokens = nested_bag.split(' ')
                count = nested_bag_tokens.pop(0)
                nested_bag = ' '.join(nested_bag_tokens)

                self.bag_graph[bag][nested_bag] = count

    def buildGoldList(self):
        self.gold_list = self.getBags('shiny gold')
        for bag in self.gold_list:
            new_bags = self.getBags(bag)
            for new_bag in new_bags:
                if new_bag not in self.gold_list:
                    self.gold_list.append(new_bag)

    def getBags(self, bag_color):
        bag_list = []
        for bag, contents in self.bag_graph.items():
            if bag_color in contents:
                bag_list.append(bag)
        return bag_list


def main():

    bag_builder = BagBuilder()
    bag_builder.buildGraph()
    bag_builder.buildGoldList()

    part1 = len(bag_builder.gold_list)

    print('Got bags?')

    # part2 = getAllYesAnswers(getGroups())
    #
    print(f'Answer 1: {part1}')
    # print(f'Answer 2: {part2}')


if __name__ == '__main__':
    main()