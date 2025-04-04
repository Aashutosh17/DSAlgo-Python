# O(n) - no of operation and no of inputs goes proportional
def print_items(n):
    for i in range (n):
        print(i)

print_items(10)

# O(n2)- You can find Nested loop, and It is considered to be worst case in Big O
def print_items(n):
    for i in range (n):
        for j in range (n):
            print(i,j)

print_items(3)

# O(1) - The Best case. The operation remains constant no matter whats the input size
def add_items(n):
    return n+n
print(add_items(4))


# O(log n) - Binary searching
# O(n log n) - You can find this with sorting algorithms (Merge sort and quick sort)

