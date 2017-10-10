
def merge(arr1, arr2):
	i = 0
	j = 0
	merged = []
	# print "arr1: {} arr2: {}".format(arr1, arr2)
	while i < len(arr1) and j < len(arr2):
		if arr1[i] > arr2[j]:
			merged += [arr2[j]]
			j += 1
		elif arr1[i] < arr2[j]:
			merged += [arr1[i]]
			i += 1
		else:
			merged += [arr1[i], arr2[j]] 
			i += 1
			j += 1

	if i < len(arr1):
		return merged + arr1[i:]
	elif j < len(arr2):
		return merged + arr2[j:]
	else:
		return merged

def sort(arr):
	if len(arr) == 1:
		return arr
	if len(arr) == 0:
		return []
	i = len(arr)/2
	return merge(sort(arr[:i]), sort(arr[i:]))

# 4 1 3 8 3 2 7
# 4 1 3 -> [1,3,4]
# 8 3 2 7 -> [2,3,7,8]
print sort([5,4,3,2,7])
print merge([1,3,4],[2,3,7,8]) # 1,2,3,3,4,7,8

