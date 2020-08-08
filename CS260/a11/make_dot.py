# abs358@drexel.edu

from bst import *
import sys

def format_node(node, identifier):
	nodeval = "Null" if (node == None) else str(node)
	nodestr = "\t" + "node_" + identifier + " [label=\"" + nodeval + "\""
	nodestr += ", shape=none" if (nodeval == "Null") else ""
	nodestr += "]\n"
	return nodestr

def do_the_thing(node, identifier):
	if node == None:
		return format_node(node, identifier)
	else:
		return do_the_thing(node.getLeft(), identifier + "l") + \
			do_the_thing(node.getRight(), identifier + "r") + \
			format_node(node, identifier) + \
			"\t" + "node_" + identifier + " -> " + "node_" + identifier + "l\n" + \
			"\t" + "node_" + identifier + " -> " + "node_" + identifier + "r\n"

if __name__ == "__main__":
	print("Enter lsit of integers (space separated):")
	bst_input = sys.stdin.readline()[:-1]
	print("Enter target file (file.dot):")
	file_name = sys.stdin.readline()[:-1]
	
	tree = BST()
	for i in bst_input.split():
		tree.insert(int(i))
	
	with open(file_name, "w") as f:
		f.write("digraph{\n")
		f.write(do_the_thing(tree.getRoot(), ""))
		f.write("}\n")
	
	print("Dot code saved in " + file_name)
