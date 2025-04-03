def Duplicates_num():
    a = [ 2,3,2,4,5,6]
    a.sort()
    for i in range (1, len(a)):
        if a[i] == a[i - 1]:
            return True

    return False

result = Duplicates_num()
print(result)