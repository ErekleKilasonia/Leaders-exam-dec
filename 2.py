from math import floor
def sum_positives_floor(listn):
    return sum([floor(i) for i in listn if i > 0])
print(sum_positives_floor([1, -4, 7, 12]))
print(sum_positives_floor([-1.5, 2.7, -3.3, 4.8]))
print(sum_positives_floor([]))
print(sum_positives_floor([-1, -2, -3]))
