import unittest
import day09


class TestDay09(unittest.TestCase):

    def test_part1(self):
        cypher = day09.XmasCypher(max_length=5, filename='test_input.txt')
        result = cypher.part1()

        self.assertEqual(127, result)

    def test_part2(self):
        cypher = day09.XmasCypher(max_length=5, filename='test_input.txt')
        result = cypher.part2()

        self.assertEqual(62, result)
