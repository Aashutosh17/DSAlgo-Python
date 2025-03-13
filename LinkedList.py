class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self,value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return True

    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def get (self, index):
        if index<0 or index >= self.length:
            return None
        temp = self.head
        for _ in range (index):
            temp = temp.next
            return temp

    def set_value (self,index,value):
        temp = self.get (index)
        if temp:
            temp.value = value
            return True
        return False

    def insert (self,index,value):
        if index <0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get (index.next)
        temp.next = new_node
        self.length += 1
        return True
  




# l1 = LinkedList(5)
# l1.append(6)
# l1.printlist()







