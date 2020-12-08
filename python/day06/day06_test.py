import unittest
from . import day06
from common import splitObjects

class TestDay6(unittest.TestCase):
    def setUp(self) -> None:
        self.input_str = """abc

a
b
c

ab
ac

a
a
a
a

b"""


    def test_splitObjects(self):
        groups = splitObjects(self.input_str)
        self.assertEqual(5, len(groups))


    def test_getDistinctYesAnswers(self):
        groups = splitObjects(self.input_str)
        result = day06.getDistinctYesAnswers(groups)
        self.assertEqual(11, result)


    def test_getAllYesAnswers(self):
        groups = splitObjects(self.input_str)

        result = day06.getAllYesAnswers(groups)
        self.assertEqual(6, result)
