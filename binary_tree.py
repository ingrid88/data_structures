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
import math

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


	def number_of_rows(self, row_values=[], count=1):
		new_row_values = []
		for node in row_values:
			if node.children is not None:
				for child in node.children:
					new_row_values.append(child)

		if len(new_row_values) == 0:
			return count
		return self.number_of_rows(new_row_values, count+1)


	def max_depth_number_of_rows(self, node, count=0):
		# gets the max depth path from a specific node
		# return depth from specified node
		if node.children is None:
			return count
		else:
			first_child = node.children[0] if node.children[0] is not None else None
			second_child = node.children[1] if node.children[1] is not None else None
			return max(
				self.max_depth_number_of_rows(first_child, count + 1), 
				self.max_depth_number_of_rows(second_child, count + 1)
			)
		pass



	def print_tree_recursively(self, row_values=[], count=1):
		new_row_values = []
		s = ''
		for node in row_values:
			s += str(node.value)+" "
			if node.children is not None:
				for child in node.children:
					new_row_values.append(child)
		print s
		if len(new_row_values) == 0:
			return 
		return self.print_tree_recursively(new_row_values, count+1)


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
			count += 1	
		print values
		print len(values)	
		rows = int(math.floor(math.log(len(values)-1,2))+1)
		print "there are {} rows".format(rows)
		for i in range(rows):
			# print "row # is {}".format(i)
			power = 2**i
			# pdb.set_trace()
			print " ".join(str(x) for x in values[:power])
			values = values[power:]


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
t.add_node(3)
t.add_node(2)
t.add_node(100)
t.add_node(8)
t.add_node(3)
t.add_node(3)
t.add_node(2)
t.add_node(1)
t.add_node(8)
t.add_node(3)
t.add_node(3)
# t.print_tree()
t.print_tree_recursively([t.head])

print "there are {} rows".format(t.number_of_rows([t.head]))
print t.max_depth_number_of_rows(t.head)


	# def calculate_rows(self):		
	# 	nodes = [self.head]
	# 	values = [self.head.value]
	# 	count = 0
	# 	while len(nodes) > 0:
	# 		parent = nodes.pop(0)
	# 		if parent.children is not None:
	# 			for child in parent.children:
	# 				if child is not None:
	# 					nodes.append(child) 
	# 					values.append(child.value)
	# 	return math.floor(math.log(len(values)-1,2))+1