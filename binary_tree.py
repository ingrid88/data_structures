# Binary Tree: a data structure in which a record is linked to two successor records, 
# usually referred to as the left branch when greater 
# and the right when less than the previous record.

#### Eg binary tree
#.     4
#.   /   \
#.  5     2
#. / \   / \
# 9   3 2   1
import pdb

class Tree(object):

	def __init__(self, head=None):
		self.head = head

	def add_node(self, value=None):
		# Algorithm: 
		# if no head, then add as head
		# if first node has no children, add it
		# if it does, pop it off and check if it has 2
		# if it has 2, append them to the nodes
		# if it doesn't, add the last child to the node 
		placed = False
		if self.head is None:
			self.head = Node(value)
		else:
			nodes = [self.head]
			while placed == False:
				if  nodes[0].children is None:
					nodes[0].children = [Node(value)]
					placed = True
				else:
					children = nodes.pop(0).children
					if len(children) < 2:
						children.append(Node(value))
						placed = True
					else:
						nodes.append(children[0])
						nodes.append(children[1])


	def print_tree(self):
		nodes = [self.head]
		values = [self.head.value]
		count = 0
		while len(nodes) > 0:
			parent = nodes.pop(0)
			if parent.children is not None:
				for child in parent.children:
					if child is not None:
						nodes.append(child) 
						values.append(child.value)
			power = 2**count
			count += 1		
			print (" "*count).join([str(x) for x in values[0:power]])
			values = values[power::]


	def breadth_first_search(self, value):
		h = self.head
		nodes = [h]
		while len(nodes) > 0:
			node = nodes.pop(0)
			print node
			if node.value == value:
				return node
			else:
				nodes.append(node.children)
				print nodes
		return False


	def depth_first_search(self, value):
		pass
	# median, mode, mean, find node, reorder, p



class Node(object):

	def __init__(self, value=None, parent=None, children=None):
		self.value = value
		self.parent = parent
		self.children = children
	
	def add_child(self, child):
		pass
	def get_child(self, child):
		pass

		
####
#.         4
#.       /   \
#.      5     2
#.    /   \   / \
#    9     3 2   1
#   / \   /
#  8   3 13

t = Tree()
t.add_node(4)
t.add_node(5)
t.add_node(2)
t.add_node(9)
t.add_node(3)
t.add_node(2)
t.add_node(1)
t.add_node(8)
t.add_node(3)
t.add_node(13)
t.print_tree()
