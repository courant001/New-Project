import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("tag", "This is a test", [None], {"href": "https://www.google.com", "target": "_blank",})
        node2 = HTMLNode("tag", "This is a test", [None], {"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(node, node2)
        node3 = HTMLNode("t", "This is a test", None, {
            "href": "https://www.google.com",
            "target": "_blank",
        })
        
        self.assertNotEqual(node, node3)

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        node2 = LeafNode("b", "Hello, world!")
        self.assertEqual(node2.to_html(), "<b>Hello, world!</b>")
        node3 = LeafNode("i", "Hello, world!")
        self.assertEqual(node3.to_html(), "<i>Hello, world!</i>")
        
class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
    )

if __name__ == "__main__":
    unittest.main()
