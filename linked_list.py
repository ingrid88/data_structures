import copy
# single linked
# Think of this as a dictionary, set, map
class List(object):
	def __init__(self, head=None):
		self.head = head

	def add_value(self, value):
		n = Node(value)
		if self.head is not None:
			n.next = self.head	
			self.head = n
		else:
			self.head = n

	def add_to_tail(self, value):
		h = self.head
		if h is None:
			self.add_value(value)	
		else:			
			while h.next is not None:
				h = h.next
			n = Node(value)	
			h.insert_node(n)

	def remove_value(self, value):
		h = self.head

		# head case
		if h.value == value:
			self.head = h.next

		while h is not None:
			# middle/tail case
			if h.next is not None:
				if h.next.value == value:
					h.next = h.next.next
					return
			h = h.next

	def reverse(self):
		h = self.head
		while h is not None:
			end = h.value
			self.remove_value(h.value)
			self.add_value(end)
			h = h.next		

	def reverse_pointers(self):
		n1 = self.head
		n2 = n1.next 
		n3 = n1.next.next
		while n3 is not None:
			n2.next = n1
			if n1 == self.head:
				n1.next = None
			n1 = n2
			n2 = n3
			n3 = n3.next
		n2.next = n1
		self.head = n2


	def contains_value(self,value):
		h = self.head
		while h is not None:
			if h.value == value:
				return True
			h = h.next		
		return False

	def value_nth_from_end(self, n):
		count = 0
		h = self.head
		while h is not None:
			count += 1
			h = h.next	

		nth_from_end = count - n
		if nth_from_end < 0:
			return None
		h = self.head
		new_count = 0
		while h is not None:
			if new_count == nth_from_end:
				return h.value
			new_count += 1
			h = h.next	

	def print_list(self):
		h = self.head
		if h is None:
			print "None"
		else:
			s = str(h.value)
			while h.next is not None:
				h = h.next
				s += " --> " + str(h.value)
			print s


class Node(object):

	def __init__(self, value=None, next_node=None):
		self.value=value
		self.next=next_node

	def insert_node(self, node):
		if self.next is None:
			self.next=node
		else:
			node.next = self.next
			self.next=node



l = List()
l.add_value(0)
l.add_value(1)
l.add_value(2)
l.add_value(5)
l.add_value(4)
l.add_value(3)
l.print_list()
l.reverse()
l.print_list() # 1

# l = List()
# l.add_value(0)
# l.add_value(1)
# l.add_value(2)
# l.print_list() # 1
l.reverse_pointers()
l.print_list() # 1


		