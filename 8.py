def longest_cons(listn):
    lstn = [sorted(listn)[0]]
    for i in range(len(listn)-1):
        if sorted(listn)[i] + 1 == sorted(listn)[i+1]:
            lstn.append(sorted(listn)[i+1])
    return len(lstn)
print(longest_cons([100, 4, 200, 1, 3, 2]))
print(longest_cons([0, 0]))
print(longest_cons([9, 1, 4, 7, 3, 2, 8, 5, 6]))