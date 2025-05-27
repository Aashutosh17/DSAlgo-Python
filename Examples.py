"""def paperwork(n, m):
    if n<0 or m<0:
        return 0
    else:
        total_blankPg = m * n
        print(total_blankPg)

paperwork(10,5)

def past(h, m, s):
    h = h * 60 * 60 * 1000
    m = m * 60 * 1000
    s = s * 1000
    return h + m + s

total = past(0,1,1)
print(total)

def solution(string1, String2):
    print(string1, String2[::-1])

solution("Word", "World")



def square_sum(numbers):
    total = 0
    for num in numbers:
        total += num * num
    return total


print(square_sum((1, 2, 2,4)))
"""

"""
def count_alphabets(string):
    SeenWords = []
    for char in string:
        if char in SeenWords:
            return True
        SeenWords.append(char)
    return False


# print(count_alphabets("word"))

User1 = {"University": "Clark",  "Address" : "950 main Street"}
User2 = User1
User2["University"] = "Northeastern"""

a =[2,4,9,7,4]
n = 5
max = 0
min = 1
for i in range (n):
    if a [i]>max:
        max = a[i]  #9
for i in range (n):
    if a[i]<min:
        min = a[i]  #2
# print(max)
# print(min)


# Insertion Sort
A = [2,4,9,7,4]

for i in range(len(A)):
    key = A[i]
    j = i-1

    while j>0 and A[j]>key:

        A[j+1] = A[j]
        j = j-1

    A[j+1] =key
print(A)


























