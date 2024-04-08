import unittest
from outlinemarkdown import markdown_to_blocks
from outlinemarkdown import block_to_blocktype
from outlinemarkdown import (block_to_quote,
                            block_to_ordered_list,
                            block_to_unordered_list,
                            block_to_code,
                            block_to_heading,
                            block_to_paragraph,
                            markdown_to_html_node)
from outlinemarkdown import (
    block_type_code,
    block_type_paragraph,
    block_type_heading,
    block_type_ordered_list,
    block_type_unordered_list,
    block_type_quote
)

from htmlnode import LeafNode,ParentNode


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self): 
        markdown = """This is **bolded** paragraph     

    This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line   
 






* This is a list
* with items   



"""
        test = markdown_to_blocks(markdown)
        self.assertEqual(test,['This is **bolded** paragraph', 'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line', '* This is a list\n* with items'])



class TestBlockToBlocktype(unittest.TestCase):
    def test_block_to_blocktype(self):
        block = "###### this is a heading"
        result = block_to_blocktype(block)
        self.assertEqual(result,block_type_heading)
        
        block2 = "```this is code```"
        result2 = block_to_blocktype(block2)
        self.assertEqual(result2,block_type_code)
        
        block3 = """>quote
>morequote
>even more"""
        result3 = block_to_blocktype(block3)
        self.assertEqual(result3,block_type_quote)
        
        block4 = """-cheese
-bread
-potato"""
        result4 = block_to_blocktype(block4)
        self.assertEqual(result4,block_type_unordered_list)

        block5 = """1. cheese
2. bread
3. potato"""
        result5 = block_to_blocktype(block5)
        self.assertEqual(result5,block_type_ordered_list)

        block6 = "nope"
        result6 = block_to_blocktype(block6)
        self.assertEqual(result6,block_type_paragraph)
        
class TestBlockToQuote(unittest.TestCase):
    def test_block_to_quote(self):
        block = """>**test**
>more quote
>even more"""
        result = block_to_quote(block)
        
     
        
     
        self.assertEqual(result, ParentNode("blockquote", [LeafNode("b",'test', None), LeafNode(None,' more quote even more', None),]))
       
class TestBlockToOrderedList(unittest.TestCase):
    def test_block_to_ordered_list(self):
        block = """1. Cheese
2. bread
3. potato"""
        result = block_to_ordered_list(block)
        
        self.assertEqual(result, ParentNode("ol",[
            ParentNode("li", [LeafNode(None,"Cheese",None)]),
            ParentNode("li", [LeafNode(None,"bread",None)]),
            ParentNode("li", [LeafNode(None,"potato",None)])
        ]))

class TestBlockToUnorderedList(unittest.TestCase):
    def test_block_to_unordered_list(self):
        block = """- Cheese
- bread
- potato"""
        result = block_to_unordered_list(block)
        
        self.assertEqual(result, ParentNode("ul",[
            ParentNode("li", [LeafNode(None,"Cheese",None)]),
            ParentNode("li", [LeafNode(None,"bread",None)]),
            ParentNode("li", [LeafNode(None,"potato",None)])
        ]))






class TestBlockToCode(unittest.TestCase):
    def test_block_to_code(self):
        block = """```def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

nums = [1, 2, 3, 4, 5]
print("The sum is:", calculate_sum(nums))
```"""
        result = block_to_code(block)
        
        expected_result = ParentNode("pre", [ParentNode("code", [LeafNode(None, """def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

nums = [1, 2, 3, 4, 5]
print("The sum is:", calculate_sum(nums))
""",None)])])
        
        self.assertEqual(result,expected_result)


class TestBlockToHeading(unittest.TestCase):
    def test_block_to_heading(self):
        block = "### this is a heading"
        result = block_to_heading(block)
        expected_result = ParentNode("h3",[LeafNode(None,"this is a heading",None)])
     
        self.assertEqual(result, expected_result)

class TestBlockToParagraph(unittest.TestCase):
    def test_block_to_paragraph(self):
        block = "this is just a paragraph with **some***inline*markdown"
        result = block_to_paragraph(block)
        expected_result = ParentNode("p",[LeafNode(None,"this is just a paragraph with "),LeafNode("b","some"),LeafNode("i","inline"),LeafNode(None, "markdown")])
        
        self.assertEqual(result,expected_result)

class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_markdown_to_html_node(self):
        markdown_content = """
# My Markdown Document

This is a simple paragraph to start off our document. It shows how a basic text block is converted.

## Lists

- Item one in an unordered list
- Item two in an unordered list

1. Item one in an ordered list
2. Item two in an ordered list

## Quote

> This is a blockquote. It should be enclosed in a `<blockquote>` tag.

## Code

Here's some code:

const exampleFunction = () => {
    console.log("Hello, world!");
    }


This should be wrapped in `<pre><code>` tags.

## Heading and Paragraph

### This is an H3 heading

And this is another paragraph, following the H3 heading.

Enjoy testing your function with this markdown document!
"""
        result = markdown_to_html_node(markdown_content)
        


if __name__ == "__main__":
    unittest.main()

