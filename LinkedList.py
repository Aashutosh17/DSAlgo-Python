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
        self.next = None

# Now here I have created one linkedlist constructor
class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):       # Added one print_list to print all value in LL
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append (self,value):
        new_node = Node(value)
     # Let's Write one edge case What if No Nodes are available Head and tail will be the same node
        if self.head is None:
         self.head = new_node
         self.tail = new_node
        else: # Here Our Main Append Logic
            self.tail.next = new_node
            self.tail = new_node
            self.length =+ 1
        return True # Optional, But Later We will write another method that will call append method







