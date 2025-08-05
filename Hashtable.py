class Hashtable:
    # constructor
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self,key):
        my_hash = 0
        for letter in key:
           my_hash = (my_hash + ord(letter)*23) % len(self.data_map)
        return my_hash

    def print_table (self):
        for index, value in enumerate(self.data_map):
            print(index, ":", value)

    # Set
    def set_item(self, key, value):
        index = self.__hash(key) # this is where to place
        if self.data_map[index] is None:
            self.data_map[index] = [] # initializing Exmpty list
        self.data_map[index].append([key,value])


my_hash_table = Hashtable()
my_hash_table.set_item('bolts',140)
my_hash_table.set_item('nails',200)
my_hash_table.set_item('Paint',500)
my_hash_table.print_table()