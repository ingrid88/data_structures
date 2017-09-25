

def unique_times(l):
	s = []
	for t in l:
		s = s + range(t[0], t[1])
	return len(set(s))

def unique_times_2(l):
	# algorithm
	# sort the tuples smallest to greatest by first item
 	is_sorted = False	
	while is_sorted == False:
		for i, t in enumerate(l[0:-1]):
			if t[0] > l[i + 1][0]:
				#switch them
	# run again through and merge each if they overlap
	for i, t in enumerate(l[0:-1]):
		print "t {}".format(t) 
		print l[i+1]
	pass

s = [(0,15),(10,25), (29, 40), (35, 80), (50, 60), (22, 55)]
# s = [(0,15),(10,25), (22, 55), (29, 40), (35, 80), (50, 60)]
# s = [(0,15),(10,25), (22, 55), (29, 40), (35, 80), (50, 60)]

print unique_times(s)

unique_times_2(s)


# 2. Interest example: circular array of relative indices is composed of a single complete cycle
#     1. Algorithm:
#         1. If the # of steps is == # of unique values and we visited unique values, then yes, else no. But this depends on the length of the circular array 
#         2. Or once you hit the same value twice, return as false 
#         3. Do you have to follow the path?
def circular_array(a):
	node = 0
	count = 0
	is_duplicate = False
	while is_duplicate == False or count < len(a):
		current_pos = (0 + a[0]) % len(a) 
		a[len(a) % (0 + a[0])]
	pass


a = [3,4,5,2,1,5]

# path is 3 --> 2 --> 5 --> 1
# 4 is missed, 5 is missed


If a=1, b=2, c=3,....z=26. Given a string, find all possible codes that string can generate. Give a count as well as print the strings.

For example:
Input: "1123". You need to general all valid alphabet codes from this string.

Output List
aabc //a = 1, a = 1, b = 2, c = 3
kbc // since k is 11, b = 2, c= 3
alc // a = 1, l = 12, c = 3
aaw // a= 1, a =1, w= 23
kw // k = 11, w = 23