def common(list1,list2):
    listn = []
    for i in list1:
        if i in list2 and i not in listn:
            listn.append(i)
    return listn
print(common([1, 2, 3], [2, 3, 4]))
print(common([1, 1, 2], [1, 3]))
print(common([], [1, 2]))
