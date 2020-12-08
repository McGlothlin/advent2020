import unittest
import day07


class TestDay07(unittest.TestCase):

    def test_findGoldBag(self):
        bag_builder = day07.BagBuilder('test_input.txt')

        bag_builder.build()
        bag_builder.findGoldBag()
        bags_with_gold = bag_builder.getGoldBags()

        self.assertEqual(4, len(bags_with_gold))
