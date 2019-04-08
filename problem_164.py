# You are given an array of length n + 1 whose elements belong to the set {1, 2, ..., # n}. By the pigeonhole principle, there must be a duplicate. Find it in linear time  # and space.
#
# Approaches:
# 1. Dictionary:
# 	- Create a empty dictionary that checks for elements
#		* Add if not present
# 	- Return element if in dict
# 	- Time: O(n)
#	- Space: n

def repeating(arr):

	dups = []
	
	for i in range(0, len(arr)):
		if abs(arr[i]) == len(arr):
			el = -1
		else:
			el = arr[abs(arr[i])]
			
		if el >= 0:
			arr[abs(arr[i])] = -arr[abs(arr[i])]
		else:
			if abs(arr[i]) == len(arr):
				dups.append(0)
			else:
				dups.append(abs(arr[i]))
	return dups
		
test1 = [1, 3, 5, 7, 2]
print(repeating(test1))
