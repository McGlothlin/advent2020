import unittest
import day07


class TestDay07(unittest.TestCase):

    def setUp(self) -> None:
        self.bag_builder = day07.BagBuilder('test_input.txt')
        self.bag_builder.buildGraph()
        self.bag_builder.buildGoldList()

    def test_findGoldBag(self):
        bags_with_gold = len(self.bag_builder.gold_list)

        self.assertEqual(4, bags_with_gold)

    def test_listSize(self):
        # Two bags contain no other bags. Therefore, we do not really care about these in our top level bag list.
        self.assertEqual(9, len(self.bag_builder.bag_graph))


    def test_getBagCount(self):
        # New bag builder instance with different input
        bag_builder = day07.BagBuilder('test_input2.txt')
        bag_builder.buildGraph()
        count = bag_builder.getBagCount('shiny gold')
        self.assertEqual(126, count)

        # count = self.bag_builder.getBagCount('shiny gold')
        # self.assertEqual(32, count)
