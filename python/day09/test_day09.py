import unittest
import day09


class TestDay08(unittest.TestCase):

    def test_execute(self):
        cypher = day09.XmasCypher(max_length=5, filename='test_input.txt')
        result = cypher.part1()

        self.assertEqual(127, result)
