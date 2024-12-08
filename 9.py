def range_non_prime(start,end):
    return [i for i in range(start,end+1) if not prime(i)]
def prime(x):
    if x < 2:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

print(range_non_prime(10,20))
print(range_non_prime(1,10))
print(range_non_prime(20,30))
print(range_non_prime(24,25))
print(range_non_prime(1,1))