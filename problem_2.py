'''Given an array of integers, return a new array such that each element at
index i of the new array is the product of all the numbers in the original
array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be
 [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would
 be [2, 3, 6].

 Follow-up: what if you can't use division?
 '''


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

Division #Wow, I didn't read the part about division, so now I know 1 way to solve this.
1. Create empty list to store output
2. Create k = p[0] * p[1]... p[n]
    a. This is a for loop or I can use np.prod
    b. Initialize k = 1
3. For loop that divides k by each element in list
    a. return k
'''

a = [3, 2, 1]

def list_mul(list):
    result = []
    k = 1

    for i in list:
        k *= i
    for i in list:
        result.append(k/i)

    return k, result

print(list_mul(a))

