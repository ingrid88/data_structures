
def bfs(graph, n):
	queue=[n]
	visited = [n]
	print n
	while len(queue) > 0:
		pos = queue.pop()
		nodes = graph[pos]
		for node in graph[pos]:
			if node not in visited:
				print node
				visited += [node]
				queue += [node]
		# print queue

def dfs(graph, n, visited=[1]):
	print n

	if len(visited) == len(graph.keys()):
		return

	children = graph[n] 
	# visited += [n]
	for child in children:
		if child not in visited:
			dfs(graph, child, visited + [child])
			return


graph = { 1 : [2,3], 2 : [1,4], 3 : [1, 4], 4: [2,3] }

#bfs(graph, 1)
#dfs(graph, 1) # 1, 2, 4, 3
dfs(graph, 1)
#bfs(graph, 1) # 1, 2, 3, 4 

