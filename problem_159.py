# 159 [Easy]

# Given a string, return the first recurring character in it, or null if there is no recurring character.
# For example, given the string "acbbac", return "b". Given the string "abcdef", return null.

# Approach:
#
# 1. Hash table:
# 		- Create a empty hash table
#		- Iterate through list
#			* If new item store in hash table
#			* If item encountered return item
#		- Time: O(n)
#		- Space: O(n)


def recurring_char(str):
	
	encountered = {}
	
	for char  in str:
		if char in encountered:
			return char
		else:
			encountered[char] = 1
	return None
	
	
test_1 = 'abcbac' # b
test_2 = 'abcdef' # None
test_3 = 'abcdea' # a

print(recurring_char(test_1))
print(recurring_char(test_2))
print(recurring_char(test_3))
