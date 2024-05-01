import unittest
from unittest.mock import mock_open, patch
from Source.ComputeEngine import ComputeEngine
from Source.Component import UnprocessedComponent, DummyComponent, RootComponent, Component

class TestComputeEngine(unittest.TestCase):
    def setUp(self):
        # test based on a sample tree

        self.L = Component("L", 0.2, None, None, None)
        self.R = Component("R", 0.3, None, None, None)
        self.O = Component("O", 0.1, None, None, None)
        self.T = Component("T", 0.5, None, None, None)
        self.D3 =  DummyComponent("D3", None, self.O, self.T, "OR")
        self.D2 =  DummyComponent("D2", None, None, self.D3, "AND")
        self.D1 = DummyComponent("D1", None, self.L, self.R, "AND")
        self.root = RootComponent("root", None, self.D1, self.D2, "AND")
        self.engine = ComputeEngine(self.root)
        self.engine.evaluate(self.root)

    def test_D3(self):
        self.assertEqual(self.D3.get_probability(), 0.55)

    def test_D2(self):
        self.assertEqual(self.D2.get_probability(), 0.55)

    def test_D1(self):
        self.assertEqual(self.D1.get_probability(), 0.06)

    def test_root(self):
        self.assertEqual(self.root.get_probability(), 0.033)

if __name__ == '__main__':
    unittest.main()