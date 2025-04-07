def Anagram (s, t):

    list1 = list(s)
    list2 = list(t)
    list1.sort()
    list2.sort()
    # return list1 == list2
    if list1 != list2:
        return False
    if list1 == list2:
        return True


results = Anagram("Mam", "kam")
print(results)








