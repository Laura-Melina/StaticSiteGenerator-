import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    

class TestLeafNode(unittest.TestCase):
    def test_leafnode(self):
        leaf = LeafNode("p", "This is a paragraph of text.")
           
        self.assertEqual(
            leaf.to_html(),
            "<p>This is a paragraph of text.</p>"
        )
        
        
        leaf2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})   
        
        self.assertEqual(
            leaf2.to_html(),
            "<a href=\"https://www.google.com\">Click me!</a>"
        )
       

        leaf3 = LeafNode(None,"Click me!", {"href": "https://www.google.com"})
        
        self.assertEqual(
            leaf3.to_html(),
            "Click me!"

        )
        


class TestParentNode(unittest.TestCase):
    
    def test_parentnode(self):
        node2 = ParentNode(
        "p",
            [
                ParentNode(
                "b",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
                ),
                ParentNode(
                "i",
                [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ],
                )
            ],
        )
        self.assertEqual(
            node2.to_html(),
            "<p><b><b>Bold text</b>Normal text<i>italic text</i>Normal text</b><i><b>Bold text</b>Normal text<i>italic text</i>Normal text</i></p>"
        )

       

        
       





if __name__ == "__main__":
    unittest.main()