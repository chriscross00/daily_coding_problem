'''Given a list of numbers and a number k, return whether any two numbers from
the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
'''

'''Approach:
1. Iterate through list.
2. Search cor dict for i == cor
    If True: return i, j and message saying 2 numbers do add to k in list
    If False: store j in dict, where j = k - i.
Repeat steps 1 and 2.

Analysis:
Space: n, because only storing corresponding j's of i
Time: n(iterate through list) * n(iterate through corresponding dict)
'''

k = 17
list = [10, 15, 3, 7]

def correspond(value, list):
    dict_cor = {}
    for i in list:
        for key, value in dict_cor.items():
            if i == value:
                return i, value
            else:
                dict_cor[i] = k - i
    return dict_cor

k = correspond(k, list)
print(k)


#Stack overflow implementation

counter = 0
for i in list:
    if k-i in list:
        counter += 1

print(counter//2)