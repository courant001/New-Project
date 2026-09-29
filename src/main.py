from textnode import TextNode, TextType 
from content_copy import copy_content
from generate_page import *
import sys

def main():
	basepath = ""
	if len(sys.argv) < 1:
		basepath = "/"
	else:
		basepath = sys.argv[0]
	dummy = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
	print(dummy)
	copy_content("static", "public")
	generate_pages_recursive("content", "template.html", "docs", basepath)

	
main()