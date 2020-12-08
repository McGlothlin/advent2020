import re
from typing import List, Union
from common import readList


class Bag:
    def __init__(self, texture: str, color: str):
        self._texture: str = texture
        self._color: str = color
        self._contents: List[Union[Bag, List[Bag]]] = []

    @property
    def isGold(self):
        if self.texture == 'shiny' and self.color == 'gold':
            return True
        return False

    @property
    def texture(self):
        return self._texture

    @property
    def color(self):
        return self._color

    @property
    def contents(self):
        return self._contents


class BagBuilder:
    def __init__(self):
        self.input_list = readList()
        # A list of top level bags found at the start of each line
        self.top_level_bags: List[Bag] = []

    # Simple tokenizer using space ' ' as the token separator.
    def build(self):
        big_bag_pattern = re.compile(r'(^\w+ \w+) bags')
        little_bag_pattern = re.compile(r'contain (\d+ \w+ \w+) bag')  # @TODO add "no other bags"

        for line in self.input_list:
            # Split match on spaces, initialize new top level bag. There should only be one top level bag match.
            big_bag_matches = re.search(big_bag_pattern, line).group(1)
            big_bag_tokens = big_bag_matches.split(' ')
            big_bag = Bag(*big_bag_tokens)

            little_bag_matches = re.search(little_bag_pattern, line)
            if not little_bag_matches:
                # No matches found
                continue
            else:
                little_bag_matches = little_bag_matches.groups()
            for bag_string in little_bag_matches:
                big_bag_contents = []
                little_bag_tokens = bag_string.split(' ')
                count = little_bag_tokens.pop(0)

                for i in range(0, int(count)):
                    big_bag_contents.append(Bag(*little_bag_tokens))

                big_bag.contents.append(big_bag_contents)

            self.top_level_bags.append(big_bag)


    def findGoldBag(self, bag_list: List[Union[Bag, List[Bag]]] = None):
        if not bag_list:
            bag_list = self.top_level_bags

        for bag_contents in bag_list:
            if isinstance(bag_contents, list):
                return self.findGoldBag(bag_contents)
            elif isinstance(bag_contents, Bag):
                if bag_contents.isGold:
                    return bag_contents
            else:
                return None


    def getGoldBags(self):
        bags_with_gold = self.top_level_bags
        for bag in bags_with_gold:
            if not self.findGoldBag(bag.contents):
                bags_with_gold.remove(bag)

        return bags_with_gold





def main():

    bag_builder = BagBuilder()
    bag_builder.build()
    bag_builder.findGoldBag()
    bags_with_gold = bag_builder.getGoldBags()

    print('Got bags?')

    # part1 = getDistinctYesAnswers(getGroups())
    # part2 = getAllYesAnswers(getGroups())
    #
    # print(f'Answer 1: {part1}')
    # print(f'Answer 2: {part2}')


if __name__ == '__main__':
    main()