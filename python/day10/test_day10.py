import unittest
import day10


class TestDay10(unittest.TestCase):

    def test_part1(self):
        cypher = day10.DaisyChain(filename='test_input.txt')
        result = cypher.part1(min_jolt_delta=1, max_jolt_delta=3, initial_jolt=0, builtin_adapter_offset=3)

        self.assertEqual(220, result)

    # def test_part2(self):
    #     cypher = day10.XmasCypher(max_length=5, filename='test_input.txt')
    #     result = cypher.part2()
    #
    #     self.assertEqual(62, result)
