import unittest
import day08


class TestDay08(unittest.TestCase):

    def test_execute(self):
        reader = day08.AsmReader('test_input.txt')
        acc = reader.execute()

        self.assertEqual(5, acc)
