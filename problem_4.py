'''Given an array of integers, find the first missing positive integer in
linear time and constant space. In other words, find the lowest positive
integer that does not exist in the array. The array can contain duplicates and
negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should
give 3.
You can modify the input array in-place.
'''

'''Approach:
1. Have a data structure that stores i in input
2. Look for all positive integers, starting at 1
3. If we find a number that is not in the hash table we return it as answer

Data structure: Hash table
'''

def low(list):
    dict = {} * len(list)

    for pos, value in enumerate(list):
        dict[pos] = value
    return dict

test = [1, 2, 0]
print(low(test))




