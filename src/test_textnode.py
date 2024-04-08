import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
        node3 = TextNode("This is a text node", "bold",None)
        node4 = TextNode("This is a text node", "bold",None)
        self.assertEqual(node3, node4)
        node5 = TextNode("This is a text node", "bold")
        node6 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node5, node6)
        node7 = TextNode("This is a text node", "bold")
        node8 = TextNode("This is a text", "bold")
        self.assertNotEqual(node7, node8)
        node9 = TextNode("This is a text node", "bold",None)
        node10 = TextNode("This is a text node", "bold","Not None")
        self.assertNotEqual(node9, node10)


if __name__ == "__main__":
    unittest.main()
