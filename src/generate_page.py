from markdown_to_html_node import *
from htmlnode import *
import os
from pathlib import Path
def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as file:
        stored_from = file.read()
    with open(template_path) as file:
        template = file.read()
    from_node = markdown_to_html_node(stored_from)
    content = from_node.to_html()
    title = extract_title(stored_from)
    page = template.replace("{{ Title }}", title)
    page = page.replace("{{ Content }}", content)
    page = page.replace('href="/', 'href="{basepath}')
    page = page.replace('src="/', 'src="{basepath}')
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, mode="w") as file:
        file.write(page)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for item in os.listdir(dir_path_content):
        item_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(item_path):
            if item_path[-3:] == ".md":
                generate_page(item_path, template_path, Path(dest_path).with_suffix(".html"), basepath)
        else:
            generate_pages_recursive(item_path, template_path, dest_path, basepath)