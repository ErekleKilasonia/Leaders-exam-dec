def substring(strng):
    maxs = 0
    for i in range(len(strng)):
        strn = ""
        x = 0
        while sorted(set(strn)) == sorted(strn) and i+x < len(strng): 
            if strng[i+x] in strn:
                break
            strn += strng[i+x]
            x += 1
        if len(strn) > maxs:
            maxs = len(strn)
    return maxs

print(substring("abcabcbb"))
print(substring("bbbbb"))
print(substring(""))
print(substring("pwwkew"))
