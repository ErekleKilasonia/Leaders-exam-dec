def find_mis_num(n):
    for i in range(1,len(n)+1):
        if i != sorted(n)[i-1]:
            return i
        
    
print(find_mis_num([1, 2, 4, 5]))
print(find_mis_num([3, 5, 6, 1, 2]))
print(find_mis_num([2]))
