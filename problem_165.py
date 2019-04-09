# Given an array of integers, return a new array where each element in the new array
# is the number of smaller elements to the right of that element in the original input array.
# For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:


# Approach:
#
# Naive:
# - Iterate throgh array and count all smaller elements to the right
# - For loop goes through all elements of list, left to right
# 	* 2nd for loop goes through range(i+1, len(arr))
# 	* If i > j, increase counter by 1
# - Break and append counter to 2nd arr
# Time: O(n^2)
# Space: n	
#
# Binary search tree

def solution(arr):

	counter_arr = []
	
	for index, i in enumerate(arr):
		counter = 0
		for j in range(index+1, len(arr)):
			if i > arr[j]:
				counter += 1		
		counter_arr.append(counter)
		
	return counter_arr
	
test1 = [2, 5, 6, 0, 2, 4]

print(solution(test1))

