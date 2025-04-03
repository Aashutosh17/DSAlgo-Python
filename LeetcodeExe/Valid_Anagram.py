def Anagram (text1, text2):
    text1.lower()
    text2.lower()
    list1 = list(text1)
    list2 = list(text2)
    list1.sort()
    list2.sort()
    # return list1 == list2
    if list1 != list2:
        return False
    if list1 == list2:
        return True


results = Anagram("Mam", "kam")
print(results)








