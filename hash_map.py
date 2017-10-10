
import time
hash_size = 1009
BINS = hash_size*[None]

def add(key, value):
	bucket_id = key % hash_size
	root = BINS[bucket_id]

	if root == None:
		root = Node(key, value)
		BINS[bucket_id] = root

	else:
		if get(key) is None:
			BINS[bucket_id] = Node(key, value)
			BINS[bucket_id].next = root

def get(key):
	bucket_id = key % hash_size
	root = BINS[bucket_id]

	if root == None:
		return None
	else:
		node = root
		while node is not None:
			if node.key == key:
				return node.value
			else:
				node = node.next
	return None



class Node(object):

	def __init__(self, key=None, value=None, next_node=None):
		self.key=key
		self.value=value
		self.next=next_node

add(3, "aaa")
add(404, "bbb")
add(4004, "ccc")
# print BINS
# print BINS[4].value
# print BINS[4].next.value
# print BINS[3].value#.next.value	
# print BINS[3].next.next.value	
print get(4004) # ccc
print get(5) # None