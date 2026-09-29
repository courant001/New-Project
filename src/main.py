from textnode import TextNode, TextType 
from content_copy import copy_content
from generate_page import *
def main():
	dummy = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
	print(dummy)
	copy_content("static", "public")
	generate_pages_recursive("content", "template.html", "public")

	
main()