# Linked List
# Node is not just the value, but it is also the pointer that shows us what is next?

head = {"value":11,
        "next" : { "value":3,
                   "next": {
                        "value":23,
                         "next":{
                             "value":7,
                             "next":{
                             "value": 4,
                            "next": None
                             }


                         }

                   }

        }
        }

# print(head['next']['next']['value'])  --> Output:23

# Constructor

# We created one Node class to use it multiple times
class Node:
    def __init__(self,value):
        self.value = value
        self.node = None

# Now here I have created one linkedlist constructor
class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.head = new_node

my_linkedlist = LinkedList(4)
print(my_linkedlist.head.value)



