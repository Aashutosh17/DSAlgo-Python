# Tree
Tree1 = {"value": 4,
       "left": None,
       "right": None
       }

Example_2 = {"value": 4,
       "left": {
           "Value" : 3,
           "left": None,
           "right": None},
       "right": {
           "Value" : 23,
           "left": None,
           "right": None}
}

# Terminology like Parent, Child and Siblings are to be kept in mind while visualizing a tree.

# Binary Search Tree


class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

my_tree = BinarySearchTree ()
print(my_tree.root)

