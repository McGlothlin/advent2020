import unittest
import day10


class TestDay10(unittest.TestCase):

    def test_part1(self):
        chain = day10.DaisyChain(filename='input.txt')
        result = chain.part1(min_jolt_delta=1, max_jolt_delta=3, initial_jolt=0, builtin_adapter_offset=3)

        # Using my correct answer to make sure I don't introduce a regression
        self.assertEqual(2263, result)

    def test_part2(self):
        chain = day10.DaisyChain(filename='test_input.txt')
        result = chain.part2()

        self.assertEqual(8, result)
