def anagram(str1,str2):
    return sorted(str1) == sorted(str2)

print(anagram("listen", "silent"))
print(anagram("hello", "world"))
print(anagram("triangle", "integral"))