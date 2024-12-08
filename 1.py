def sum_positives(listn):
    return sum([i for i in listn if i > 0])
print(sum_positives([1, -4, 7, 12]))
print(sum_positives([-1, -2, -3, -4]))
print(sum_positives([]))