import time
hash_size = 1009
BINS = hash_size*[None]

def add(i):
	bucket_id = i % hash_size
	root = BINS[bucket_id]
	if root == None:
		root = Node(i)
		BINS[bucket_id] = root
	else:
		if not contains(i):
			BINS[bucket_id] = Node(i)
			BINS[bucket_id].next = root


# BINS[i] = 4 -> 2 -> None

def contains(i):
	bucket_id = i % hash_size
	root = BINS[bucket_id]

	if root == None:
		return False
	else:
		node = root
		while node is not None:
			if node.value == i:
				return True
			else:
				node = node.next
	return False

class Node(object):

	def __init__(self, value=None, next_node=None):
		self.value=value
		self.next=next_node
start = time.time()

for i in range(100000):
	add(i)
for i in range(100000):
	contains(i)
end = time.time()

print(end - start)
# print BINS
# print BINS[4].value
# print BINS[4].next.value
# print BINS[3].value#.next.value	
# print BINS[3].next.next.value	
print contains(404)
print contains(4)
print contains(3)
print contains(40)
print contains(623)