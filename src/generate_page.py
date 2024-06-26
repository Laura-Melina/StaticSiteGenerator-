import os
from outlinemarkdown import markdown_to_html_node


def extract_tile(markdown):                                   # extracts the title of the markdown file
    blocks = markdown.split("\n\n")
    
    if blocks[0].startswith("#"):
        return f"{blocks[0][2:]}"
    else:
        raise Exception("All pages need a single h1 header")
    

def generate_page(from_path, template_path, dest_path):       #generates a html page by processing the markdown into html nodes which are then converted into plain html
                                                              # and then inputting the title and html text into the given html template then saving it to the destination path
    open_markdown = open(from_path, "r")
    markdown_contents = open_markdown.read()
    open_markdown.close()

    open_template = open(template_path,"r")
    template_contents = open_template.read()
    open_template.close()
    
    html_nodes = markdown_to_html_node(markdown_contents)
    html = html_nodes.to_html()
    
    title = extract_tile(markdown_contents)
    html_output = template_contents.replace("{{ Title }}", title)
    html_output = html_output.replace("{{ Content }}", html)
    
    if os.path.exists(dest_path):
        file = open(os.path.join(dest_path,"index.html"), "x")
        file.write(html_output)
        file.close()
    else :
        os.makedirs(dest_path)
        file = open(os.path.join(dest_path,"index.html"), "x")
        file.write(html_output)
        file.close()


def generate_page_recursive(dir_path_content, template_path, dest_dir_path):   #uses the functionality of the previous function but goes throught the whole folder and creates pages
    
    for entry in os.listdir(dir_path_content):
        if os.path.isfile(os.path.join(dir_path_content,entry)):
            generate_page(os.path.join(dir_path_content,entry),template_path,dest_dir_path)
        else: 
            generate_page_recursive(os.path.join(dir_path_content,entry),template_path,os.path.join(dest_dir_path,entry))