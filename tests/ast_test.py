import unittest

from project.parser import AddNode, DivNode, MultNode, NumberNode, BinaryOpNode, SubNode

class NumberNodeTest(unittest.TestCase):
    def test_instantiate_object(self):
        node = NumberNode(10)
        self.assertTrue(node)

    def test_debug_string_method(self):
        node = NumberNode(6)
        self.assertEqual(node._debug_string(), '6')

    def test_eval_method(self):
        node = NumberNode(6)
        self.assertEqual(node.eval(), 6)

class BinaryOpNodeTest(unittest.TestCase):
    def test_instantiate_object(self):
        node = BinaryOpNode(NumberNode(10), NumberNode(2))
        self.assertTrue(node)

class AddNodeTest(unittest.TestCase):
    def test_instantiate_object(self):
        node = AddNode(NumberNode(10), NumberNode(10))
        self.assertTrue(node)

    def test_debug_string_method(self):
        node = AddNode(NumberNode(7), NumberNode(4))
        self.assertEqual(node._debug_string(), '(7 + 4)')

    def test_eval_method(self):
        node = AddNode(NumberNode(7), NumberNode(4))
        self.assertEqual(node.eval(), 11)

class SubNodeTest(unittest.TestCase):
    def test_instantiate_object(self):
        node = SubNode(NumberNode(10), NumberNode(10))
        self.assertTrue(node)

    def test_debug_string_method(self):
        node = SubNode(NumberNode(7), NumberNode(4))
        self.assertEqual(node._debug_string(), '(7 - 4)')

    def test_eval_method(self):
        node = SubNode(NumberNode(7), NumberNode(4))
        self.assertEqual(node.eval(), 3)

class MultNodeTest(unittest.TestCase):
    def test_instantiate_object(self):
        node = MultNode(NumberNode(10), NumberNode(10))
        self.assertTrue(node)

    def test_debug_string_method(self):
        node = MultNode(NumberNode(7), NumberNode(4))
        self.assertEqual(node._debug_string(), '(7 * 4)')

    def test_eval_method(self):
        node = MultNode(NumberNode(7), NumberNode(4))
        self.assertEqual(node.eval(), 28)

class DivNodeTest(unittest.TestCase):
    def test_instantiate_object(self):
        node = DivNode(NumberNode(10), NumberNode(10))
        self.assertTrue(node)

    def test_debug_string_method(self):
        node = DivNode(NumberNode(7), NumberNode(4))
        self.assertEqual(node._debug_string(), '(7 / 4)')

    def test_eval_method(self):
        node = DivNode(NumberNode(2), NumberNode(2))
        self.assertEqual(node.eval(), 1)
