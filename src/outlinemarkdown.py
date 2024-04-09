import re 
from htmlnode import (LeafNode,ParentNode)
block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"
from inline_markdown import text_to_textnodes
from textnode import(text_node_to_html_node
)


def markdown_to_blocks(markdown):            #takes a string of markdown and converts it into seperate blocks
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_blocktype(block):            #takes  a markdown block and determines its type 

    pattern = r"^#{1,6} "
    if re.match(pattern,block):
        return block_type_heading
    
    if block[:3] == "```" and block[-3:] == "```":
        return block_type_code
    
    split_block = block.split("\n")
   
    result_quote = all(split[:1] == ">" for split in split_block)
    if result_quote == True:
        return block_type_quote
    
    result_unordered_list = all(split[:1] == "*" or split[:1] == "-" for split in split_block)        
    if result_unordered_list == True:
        return block_type_unordered_list

    result = True 
    for i in range(0,len(split_block)):
        x = i + 1
        
        if split_block[i][:2] == f"{x}.":
            result = True 
        else:
            result = False 
        
        if i == len(split_block)-1:
            
            if result == True:
                return block_type_ordered_list
    return block_type_paragraph



def block_to_quote(block):               # converts a block of markdown to a nested list structure of html nodes respresenting html quote
    inline = []
    split_block = block.split("\n")
   
    neat_line = []
    for split in split_block:
        neat_line.append(split[1:])
    cleared_quote = " ".join(neat_line)  
    
    
    text_nodes = text_to_textnodes(cleared_quote)
    
    
    for nodes in text_nodes:
        
        inline.append(text_node_to_html_node(nodes))
        
    output = ParentNode("blockquote",inline)

    return output

def block_to_unordered_list(block):     #converts a block of markdown to a nested list structure of html nodes represting an unordered list 
    split_block = block.split("\n")
    clean_lines = []
    for split in split_block:
        line = split[1:]
        line = line.strip()
        clean_lines.append(line)

    inline = []
    text_nodes = []
    for node in clean_lines:
        text_nodes.append(text_to_textnodes(node))

    for i in range(0,len(text_nodes)):
        inline_line = []
        for x in range(0,len(text_nodes[i])):
            inline_line.append(text_node_to_html_node(text_nodes[i][x]))

        inline.append(ParentNode("li",inline_line))

    output = ParentNode("ul",inline)
    return output


def block_to_ordered_list(block):  #converts a block of markdown to a nested list structure of html nodes represting an ordered list

    split_block = block.split("\n")
    clean_lines = []

    for i in range(0,len(split_block)):
        x = i + 1 
        line = split_block[i].replace(f"{x}.","",1)
        line = line.strip()
        clean_lines.append(line)
    
    inline = []
    text_nodes = []
    for node in clean_lines:
        text_nodes.append(text_to_textnodes(node))
    
    for i in range(0,len(text_nodes)):
        inline_line = []
        for x in range(0,len(text_nodes[i])):
            inline_line.append(text_node_to_html_node(text_nodes[i][x]))

        inline.append(ParentNode("li",inline_line))
      
    output = ParentNode("ol",inline)
   
    return output
    

def block_to_code(block):          ##converts a block of markdown to a nested list structure of html nodes represting a code block
    code_without_ticks = block.strip("`")
    return ParentNode("pre", [ParentNode("code", [LeafNode(None, code_without_ticks)])])

def block_to_heading(block):
    def count_hashes(block):
        return len(block) - len(block.lstrip("#"))
    count = count_hashes(block)

    hashes_removed = block[count + 1:]
    text_nodes = text_to_textnodes(hashes_removed)
    inline = []
    for node in text_nodes:
        inline.append(text_node_to_html_node(node))
    return ParentNode(f"h{count}",inline)

def block_to_paragraph(block):  #converts a block of markdown to a nested list structure of html nodes represting a normal paragraph
    text_nodes = text_to_textnodes(block)
    inline = []
    for node in text_nodes:
        inline.append(text_node_to_html_node(node))
    return ParentNode("p",inline)


def markdown_to_html_node(markdown):  #converts a markdown document into a nested list structure of html nodes representing the whole html structure
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)


def block_to_html_node(block):       #converts a markdown block into the correct block type
    block_type = block_to_blocktype(block)
    if block_type == block_type_paragraph:
        return block_to_paragraph(block)
    if block_type == block_type_heading:
        return block_to_heading(block)
    if block_type == block_type_code:
        return block_to_code(block)
    if block_type == block_type_ordered_list:
        return block_to_ordered_list(block)
    if block_type == block_type_unordered_list:
        return block_to_unordered_list(block)
    if block_type == block_type_quote:
        return block_to_quote(block)
    raise ValueError("Invalid block type")

