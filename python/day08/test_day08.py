import unittest
import day08


class TestDay08(unittest.TestCase):

    def test_execute(self):
        reader = day08.AsmReader(filename='test_input.txt')
        acc = reader.execute()

        self.assertEqual(5, acc)

    def test_bootCheck(self):
        reader = day08.AsmReader(filename='test_input.txt')
        acc = reader.bootCheck()

        self.assertEqual(8, acc)
