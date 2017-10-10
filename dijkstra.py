

m = [
	[0, 2, 4],
	[2, 0, 1], 
	[4, 1, 0]
]

s = 0
d = 2
n = 3

def dijkstra():
	''' 
	store nodes in array and store shortest distance to nodes in dictionary from s
	set next node as node with shortest distance in dictionary'''
	pass

def get_shortest(m, s, d, visited=[], node=None):
	''' find all paths and return shortest and keep track of visited in each iteration
	'''
	# import pdb;pdb.set_trace()
	print "s: {} d: {}".format(s, d)
	if node == d:
		return 0
	# print node

	if node == None:
		children = [x for x in range(n) if m[s][x] > 0]
		current = 0
		node = 0
		visited = [0]
	else:
		children = [x for x in range(n) if m[node][x] > 0]
		current = m[s][node] 

	# print "children {}".format(children)
	# print "visited {}".format(visited)
	return current + min([get_shortest(	
				m, 
				node, 
				d, 
				visited + [child], 
				child
			) for child in children if child not in visited])
	

print get_shortest(m, s, d)