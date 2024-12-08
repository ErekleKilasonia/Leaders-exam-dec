from itertools import permutations
def sum3(listn):
    lstn = []
    sorted_listn = []
    for i in list(permutations(listn,3)):
        if sum(i) == 0:
            if sorted(i) not in sorted_listn:
                sorted_listn.append(sorted(i))
                lstn.append(list(i))
    return lstn
print(sum3([-1, 0, 1, 2, -1, -4]))
print(sum3([0, 0, 0]))
print(sum3([1, 2, -2, -1]))