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
	def __init__(self, root=None):
		self.root = root

	def add_child(self, value=None):
		# Algorithm
		# if root doesn't exist, add it
		# if left node is empty of root, add it else try right
		# if both are full, add them to the queue and check if their children exist
		placed = False
		if self.root is None:
			self.root = Node(value)
		else:
			node_queue = [self.root]
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
		if row_values[0][0] == self.root:
			nodes = [row_values[0][0]]
			print self.root.value
		else:
			nodes = [i for sub in row_values for i in sub if i is not None]
			print " ".join("("+str(getattr(x,'value', 'None'))+" "+str(getattr(y,'value', 'None'))+")" for x,y in row_values)
		for node in nodes:
			new_row_values.append((node.left,node.right))
		if len(new_row_values) == 0:
			return 
		return self.print_tree(new_row_values)


# ALSO RETURN PARENT (DO THIS WITH DFS INSTEAD)
	def find_dfs(self, [parent], value):

		parent = parent.right == value 
		parent = parent.left == value
		return self.find_dfs([parent], value)
		while len(queue) > 0:
			node = queue.pop(0)
			if node.value == value:
				return node
			else:
				if node.left is not None:
					queue.append(node.left)
				if node.right is not None:
					queue.append(node.right)
		return None

	def find_dfs(self, value):
		queue = [self.root]
		while len(queue) > 0:
			node = queue.pop(0)
			if node.value == value:
				return node
			else:
				if node.left is not None:
					queue.append(node.left)
				if node.right is not None:
					queue.append(node.right)
		return None


	def smallest(self, smallest=None, queue=[]):
		if len(queue) == 0:
			return smallest
		else:
			node = queue.pop(0)
			if node.value < smallest.value:
				smallest = node
			for child in [node.left, node.right]:
				if child is not None:
					queue.append(child)
			return self.smallest(smallest, queue)

	def smallest_minimal(self, node):
		l = [getattr(node, 'value', 0)]
		for child in [node.right, node.left]:
			if child is not None:
				l.append(t.smallest_minimal(child))
		return min(l)

	def bfs(self):
		queue = [self.root]
		s = ""
		while len(queue) > 0:
			node = queue.pop(0)
			s += str(node.value) + " "
			for child in [node.left, node.right]:
				if child is not None:
					queue.append(child)
		return s

	def dfs(self, node):
		l = [str(node.value)]
		for child in [node.left, node.right]:
			if child is not None:
				l.append(self.dfs(child))
		return " ".join(l) 


	def delete(self):
		node = self.find(value)
		parent, position = self.find_parent(value)
		## Cases
		# if root
		if self.value == value:
			self.value = node.left
		# if has no children
		elif node.left is None and node.right is None:
			parent[position] = None
		# if has 1 child
		elif node.left is None or node.right is None:
			parent[position] = getattr(node, 'left', node.right)
		# if has 2 children
		# find smallest value in right and replace original node with it. 
		elif node.left is not None and node.right is not None:
			parent[position].right = self.smallest(node.right)
			self.smallest(smallest=node.right, queue=[node.right])

	def least_common_ancestor(self, node_1, node_2):
		# how far is node_1 from root
		r = self.root
		# Algorithm
		# how far is node_2 from root
		# get difference, go through farther one to same level as close one
		# move up and checkif parents are equal and return when parents of both are equal
		pass

	def farthest_distance_between_two_nodes(self):
		# return nodes
		pass


	def max_heap(self):
		"""Heap just guarantees that elements on higher levels are greater 
		(for max-heap) or smaller (for min-heap) than elements on lower levels, 
		whereas BST guarantees order (from "left" to "right")."""
		pass

	def min_heap(self, value):
		# this is adding a single element to a tree that maintains heap
		# Reminder: dont do min and max since they are the same
		pass

	def binary_add(self, value):
		# Algorithm:
		# is the left > right branch of this tree, 
			# if not, swap, 
		# iterate (recursively)
		pass 



class Node(object):

	def __init__(self, value=None, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

####
#.         4
#.       /   \
#.      5     2
#.    /   \   / \
#            9
t = BinaryTree()
t.add_child(4)
t.add_child(5)
t.add_child(2)
t.add_child(9)
t.add_child(3)
t.add_child(1)
# t.add_child(13)
# t.add_child(8)
# t.add_child(3)
# t.add_child(2)
# t.add_child(1)
# t.add_child(8)
# t.add_child(3)
# find()
t.print_tree([(t.root, None)])
print t.smallest(t.root, [t.root]).value
print t.smallest_minimal(t.root)
print t.dfs(t.root)
print t.bfs()
# t.find_parent(5)
# t.print_tree([(t.root, None)])

