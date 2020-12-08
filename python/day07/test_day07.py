import unittest
import day07


class TestDay07(unittest.TestCase):

    def setUp(self) -> None:
        self.bag_builder = day07.BagBuilder('test_input.txt')
        self.bag_builder.build()

    def test_findGoldBag(self):
        self.bag_builder.findGoldBag()
        bags_with_gold = self.bag_builder.getGoldBags()

        self.assertEqual(4, len(bags_with_gold))

    def test_listSize(self):
        # Two bags contain no other bags. Therefore, we do not really care about these in our top level bag list.
        self.assertEqual(7, len(self.bag_builder.top_level_bags))
