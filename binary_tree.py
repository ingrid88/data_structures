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

class BinaryTree(object):
	def __init__(self, head=None):
		self.head = head

	def add_child(self, value=None):
		# Algorithm
		# if head doesn't exist, add it
		# if left node is empty of root, add it else try right
		# if both are full, add them to the queue and check if their children exist
		placed = False
		if self.head is None:
			self.head = Node(value)
		else:
			node_queue = [self.head]
			while placed == False:
				# left is empty
				node = node_queue.pop(0)
				if node.left is None:
					node.left = Node(value)
					placed = True
				# right is empty
				elif node.right is None:
					node.right = Node(value)
					placed = True
				# both are full - 
				# 0. remove current node as potential parent
				# 1. add current node children to node_queue
				# 2. look for empty branch in node_queue
				else:
					children = [node.left, node.right]
					for child in children:
						node_queue.append(child)

	def print_tree(self, row_values=[]):
		new_row_values = []
		# pdb.set_trace()
		if row_values[0][0] == self.head:
			nodes = [row_values[0][0]]
			print self.head.value
		else:
			nodes = [i for sub in row_values for i in sub if i is not None]
			print " ".join("("+str(getattr(x,'value', 'None'))+" "+str(getattr(y,'value', 'None'))+")" for x,y in row_values)
		for node in nodes:
			new_row_values.append((getattr(node,'left', None), getattr(node,'right', None)))
		if len(new_row_values) == 0:
			return 
		return self.print_tree(new_row_values)


class Node(object):

	def __init__(self, value=None, left=None, right=None, children=None):
		self.value = value
		self.left = left
		self.right = right

####
#.         4
#.       /   \
#.      5     2
#.    /   \   / \
#    9  
t = BinaryTree()
t.add_child(4)
t.add_child(5)
t.add_child(2)
t.add_child(9)
t.add_child(3)
t.add_child(2)
# t.add_node(1)
# t.add_node(8)
# t.add_node(3)
t.print_tree([(t.head, None)])

