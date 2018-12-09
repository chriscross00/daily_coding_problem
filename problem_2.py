'''Given an array of integers, return a new array such that each element at
index i of the new array is the product of all the numbers in the original
array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be
 [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would
 be [2, 3, 6].'''


'''Approach:
List comp #I'm not strong enough in basics to do this yet, i should have 
              it explicit 
For loop #This method doesn't work because I am removing the item I am 
          trying to iterate over. This throws back the error 'for j in temp'
          that says it's not iterable.
1. Create empty list to store output
2. Create temp list that excludes item
    a. nested for loop that multiplies each element in excluded list, k
    b. return k
3. append k to stored output list
4. repeat

Create a copy
1.
'''

a = [3, 2, 1]

def exclude_multi(list):
    output = []

    for i in list:
        temp = list.remove(i)
        for j in temp:
            multiply = 1
            multiply *= j
            output.append(multiply)
    return output

exclude_multi(a)

