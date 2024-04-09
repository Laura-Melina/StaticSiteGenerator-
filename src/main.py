from textnode import TextNode
import os,shutil
from static_to_public import copy_static_to_public
from generate_page import generate_page_recursive

dir_path_static = "./static"
dir_path_public = "./public"
from_path = "./content"
template_path = "./template.html"
dest_path = "./public"


def main(): #executs the whole programm
   
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    print("Copying static files to public directory...")    
    copy_static_to_public(dir_path_static, dir_path_public)
    generate_page_recursive(from_path,template_path,dest_path)



main()


