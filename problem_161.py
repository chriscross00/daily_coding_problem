# Given a list of words, return the shortest unique prefix of each word. 
# For example, given the list:
# dog, cat, apple, apricot, fish
#
# Return the list:
# d, c, app, apr, f

# Naive solution:
# - Start at the end of each word and remove 1 letter
# - Keep on removing until there you encounter a non-unique
# 	* Remove words from list, to checked list
# - Continue until all words are removed or 1 letter
# Time: O(n*k), where n = number of words and k = avg length of word
# Space: n

# Better solution
# Check if any words are the same, if true return False
# Sort list
# Choose the substring with the longest length



abcd
abcde
abcdef