
# median, mode, mean, find node, reorder, p


class Tree(object):

	def __init__(self, head=None):
		head = head

	def add_node(self, value=value, child=child, parent=parent):
		child = Node(value)
		if parent.children not None:
			parent.children.append(child)
		else:
			parent.children = [child]

	def print_tree(self):
		pass

	def depth_first_search(self, value):
		pass

	def breadth_first_search(self, value):
		pass


class Node(object):

	def __init__(self, value=value, parent=None, children=None):
		self.value = value
		self.parent = parent
		self.children = children
	
	def add_child(self, child):
		pass
	def get_child(self, child):
		pass

		

t = Tree()
h = Node(3)
t.head = h




