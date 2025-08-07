"""Finding common items using two methods:
one with nested loops (basic but slow),
and a better one using hash (faster and great for interviews)"""

# First Approach using nested loop
def items_in_common(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

# list1 = [2,3,4]
# list2 = [2,4,6]
# print(items_in_common(list1, list2))


# Hashtable (Recommended approach)
def items_in_common(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True

    for j in list2:
        if j in my_dict:
            return True

    return False

list1 = [2,3,4]
list2 = [1,5,6]
print(items_in_common(list1, list2))






