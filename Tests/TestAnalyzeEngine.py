import unittest
from unittest.mock import mock_open, patch
from Source.AnalyzeEngine import AnalyzeEngine
from Source.Component import UnprocessedComponent, DummyComponent, RootComponent, Component

class TestAnalyzeEngine(unittest.TestCase):
    def setUp(self):

        self.L = UnprocessedComponent("L", 0.2, None, None, None, None)
        self.R = UnprocessedComponent("R", 0.3, None, None, None, None)
        self.O = UnprocessedComponent("O", 0.1, None, None, None, None)
        self.T = UnprocessedComponent("T", 0.5, None, None, None, None)
        self.main = UnprocessedComponent("main", None, "((L AND R) AND (O OR T))", None, None, None)

        self.dic1 = {"L": self.L, "R": self.R, "O": self.O, "T": self.T, "main": self.main}
        self.engine = AnalyzeEngine()
        self.engine.createUnprocessedTree(self.dic1)

    def test_mainRel(self):
        self.assertEqual(self.engine.getRoot().get_dep_rel(), "AND")

    def test_DRel1(self):
        self.assertEqual(self.engine.getRoot().left.get_dep_rel(), "OR")

    def test_DRel2(self):
        self.assertEqual(self.engine.getRoot().right.get_dep_rel(), "AND")

    
    def test_leftRight(self):
        self.assertEqual(self.engine.getRoot().left.id, "D")
        self.assertEqual(self.engine.getRoot().right.id, "D")
    
    def test_leafNodes1(self):
        comp1 = self.engine.getRoot().left.left
        comp2 = self.engine.getRoot().left.right
        true = (((comp1.id == "T") and (comp2.id == "O")) or ((comp1.id == "O") and (comp2.id == "T")))
        self.assertTrue(true)

    def test_leafNodes2(self):
        comp1 = self.engine.getRoot().right.left
        comp2 = self.engine.getRoot().right.right
        true = (((comp1.id == "L") and (comp2.id == "R")) or ((comp1.id == "R") and (comp2.id == "L")))
        self.assertTrue(true)

if __name__ == '__main__':
    unittest.main()