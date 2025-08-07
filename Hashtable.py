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

    # Get
    def get_item(self,key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range (len(self.data_map[index])):
                if self.data_map[index] [i][0] == key:
                    return self.data_map[index] [i] [1]
        return None

    # keys
    def keys(self):
        all_keys = []
        for i in range (len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range (len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

my_hash_table = Hashtable()

# my_hash_table.set_item('bolts', 100)
# my_hash_table.set_item('nails', 200)
# my_hash_table.set_item('paints', 300)

# print(my_hash_table.keys())