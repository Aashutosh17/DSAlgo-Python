
# Classes that are going to be used mostly
class LinkList :
    # Initializer
    def __init__(self):
        pass
    def append (self, value):
        pass
    def pop (self, value):
        pass
    def prepend (self, value):
        pass
    def insert (self, index, value):
        pass
    def remove (self, index):
        pass

# Pointers
# Int
num1 = 11
num2 = num1
# print(num2) # 11
# print(id(num1))
# print(id(num2)) #Integers will be on same memory location

# But Dictionary will be different
User1 = {"University": "Clark",  "Address" : "950 main Street"}
User2 = User1
# print(User2) # It will give you User1 details
User2["University"] = "Northeastern"  # now I will change User2 University
print(User1)
print(User2)  # Now this will change User2 University and User1 University as we did User2 = User1 Make sense now right in dictionary


