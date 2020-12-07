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
        self.assertEqual(groups, 5)


    def test_getYesAnswers(self):
        groups = splitObjects(self.input_str)
        result = day06.getYesAnswers(groups)
        self.assertEqual(result, 11)
