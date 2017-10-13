



def sum_watch_times(root, add_value=True):
	total_time = 0
	node = root
	#import pdb; pdb.set_trace()

	if node is None:
		return 0

	if node.kind == 'B':
		total_time += sum([sum_watch_times(child, False) for child in node.children])
		
	if node.kind == 'W':
		if add_value:
			total_time += node.value
		total_time += sum([sum_watch_times(child, add_value) for child in node.children])

	if node.kind == 'S':
		total_time += sum([sum_watch_times(child, True) for child in node.children])

	print "value: {} and kind: {} and total_time {}".format(node.value, node.kind, total_time)
	return total_time






class Node(object):
	def __init__(self, value=0, kind=None, children=[]):
		self.value = value
		self.children = children
		self.kind = kind


if __name__ == "__main__":
  test_tree = Node(0, 'B')
  test_tree.children = [Node(0, 'S'), Node(60, 'W')]
  test_tree.children[0].children = [Node(5, 'W')]
  test_tree.children[0].children[0].children  = [Node(5, 'W'), Node(0, 'B')]
  test_tree.children[0].children[0].children[0].children  = [Node(5, 'W')]
  print sum_watch_times(test_tree, add_value=True)

"""
      B
    S   W
    Wo
  Wo  B
   W

"""