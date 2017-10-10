

m = [
	[0, 1, 5, 5],
	[1, 0, 5, 1], 
	[5, 5, 0, 1],
	[5, 1, 1, 0],
]

s = 0
d = 2
n = 4

def dijkstra(m, s, destination, visited=[], d={}):
	''' 
	store nodes in array and store shortest distance to nodes in dictionary from s
	set next node as node with shortest distance in dictionary'''
	# import pdb; pdb.set_trace()
	visited += [s]
	d[s] = m[s][s]

	while len(visited) < n:
		children = [child for child in range(n) if m[s][child] > 0 and child not in visited]

		min_distance_child = -1
		min_distance = None
		for child in children:
			if child not in d:
				d[child] = m[s][child]
			else:
				d[child] = min(d[child], d[s] + m[s][child])
			if min_distance > d[child] or min_distance == None:
					min_distance = m[s][child]
					min_distance_child = child
		s = min_distance_child
		# print s
		visited += [s]
	return d[destination]

print dijkstra(m, s, d)

def get_shortest(m, s, d, visited=[], node=None):
	''' find all paths and return shortest and keep track of visited in each iteration
	'''
	# import pdb;pdb.set_trace()
	# print "s: {} d: {}".format(s, d)
	if s == d:
		return 0
	# print node

	if node == None:
		children = [x for x in range(n) if m[s][x] > 0]
		current = 0
		node = 0
		visited = [0]
	else:
		children = [x for x in range(n) if m[node][x] > 0 and x not in visited]
		current = m[s][node] 

	if len(children) == 0:
		return current
	else:
		return current + min([get_shortest(	
					m, 
					node, 
					d, 
					visited + [child], 
					child
				) for child in children])
	

print get_shortest(m, s, d)