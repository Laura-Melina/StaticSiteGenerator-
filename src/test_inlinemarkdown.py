import unittest
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_links,
    text_to_textnodes
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_snd(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertEqual(new_nodes,
                            [
                             TextNode("This is text with a ", text_type_text),
                             TextNode("code block", text_type_code),
                             TextNode(" word", text_type_text),
                            ]
                         )
        

        node2 = TextNode("This is text with a **bold** word", text_type_text)
        new_nodes2 = split_nodes_delimiter([node2], "**", text_type_bold)
        self.assertEqual(new_nodes2,
                            [
                             TextNode("This is text with a ", text_type_text),
                             TextNode("bold", text_type_bold),
                             TextNode(" word", text_type_text),
                            ]
                         )
        
        node3 = TextNode("This is text with an *italic* word", text_type_text)
        new_nodes3 = split_nodes_delimiter([node3], "*", text_type_italic)
        self.assertEqual(new_nodes3,
                            [
                             TextNode("This is text with an ", text_type_text),
                             TextNode("italic", text_type_italic),
                             TextNode(" word", text_type_text),
                            ]
                         )
        
        

class TestExtractMarkdownImages(unittest.TestCase):
    def test_emi(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
        result = extract_markdown_images(text)
        self.assertEqual(result,[("image", "https://i.imgur.com/zjjcJKZ.png"), ("another", "https://i.imgur.com/dfsdkjfd.png")])
        




class TestExtractMarkdownLinks(unittest.TestCase):
    def test_eml(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"     
        result = extract_markdown_links(text)
        self.assertEqual(result,[("link", "https://www.example.com"), ("another", "https://www.example.com/another")])
        
class TestSplitNodesLinks(unittest.TestCase):
    def test_snl(self): 
        node = TextNode(
        "This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png)",
        text_type_text,)
        new_nodes = split_nodes_links([node])
        
        self.assertEqual(new_nodes,[
                        TextNode("This is text with an ", text_type_text,None),
                        TextNode("image", text_type_link, "https://i.imgur.com/zjjcJKZ.png"),
                        TextNode(" and another ", text_type_text,None),
                        TextNode("second image", text_type_link, "https://i.imgur.com/3elNhQu.png"
                        ),
                        ]
                        )
        node2 = TextNode("This is some random gibberish",text_type_text)
        new_nodes2 = split_nodes_links([node2])
        self.assertEqual(new_nodes2,[TextNode("This is some random gibberish",text_type_text)])
       
        node3 = TextNode(
        "[image](https://i.imgur.com/zjjcJKZ.png)[second image](https://i.imgur.com/3elNhQu.png)",
        text_type_text,)
        new_nodes3 = split_nodes_links([node3])
        self.assertEqual(new_nodes3,[TextNode("image", text_type_link, "https://i.imgur.com/zjjcJKZ.png"),TextNode("second image", text_type_link, "https://i.imgur.com/3elNhQu.png"
                        )])
        

class TestSplitNodesImage(unittest.TestCase):
    def test_sni(self): 
        node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        text_type_text,)
        node4 = TextNode("just some text",text_type_text)
        node5 = TextNode("just some other text",text_type_text)
        new_nodes = split_nodes_image([node5,node,node4])
        
        self.assertEqual(new_nodes,[
                    TextNode("just some other text",text_type_text),
                    TextNode("This is text with an ", text_type_text,None),
                    TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
                    TextNode(" and another ", text_type_text,None),
                    TextNode("second image", text_type_image, "https://i.imgur.com/3elNhQu.png"),
                    TextNode("just some text",text_type_text)
                    ]
                    )
        
        
        node2 = TextNode("This is some random gibberish",text_type_text)
        new_nodes2 = split_nodes_image([node2])
        self.assertEqual(new_nodes2,[TextNode("This is some random gibberish",text_type_text)])
        
        node3 = TextNode("![image](https://i.imgur.com/zjjcJKZ.png)![second image](https://i.imgur.com/3elNhQu.png)",
        text_type_text,)
        new_nodes3 = split_nodes_image([node3])
        self.assertEqual(new_nodes3,[TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),TextNode("second image", text_type_image, "https://i.imgur.com/3elNhQu.png"
                       )])



class TestTextToTextNodes(unittest.TestCase):
    def test_tttn(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        test = text_to_textnodes(text)
        self.assertEqual(test,
                        [
                        TextNode("This is ", text_type_text),
                        TextNode("text", text_type_bold),
                        TextNode(" with an ", text_type_text),
                        TextNode("italic", text_type_italic),
                        TextNode(" word and a ", text_type_text),
                        TextNode("code block", text_type_code),
                        TextNode(" and an ", text_type_text),
                        TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
                        TextNode(" and a ", text_type_text),
                        TextNode("link", text_type_link, "https://boot.dev"),
                        ])
        

if __name__ == "__main__":
    unittest.main() 

    