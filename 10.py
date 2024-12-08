from itertools import permutations
def edit_distance(word1,word2):
    word1 = list(word1)
    word2 = list(word2)
    counter = 0
    
    for i in word1:
        if i not in word2 or (i in word2 and word1.count(i) > word2.count(i)):
            if len(word1) <= len(word2):
                break
            word1.remove(i)
            counter += 1
    
    if sorted(word1) == sorted(word2):
        to_replace = []
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                to_replace.append(i)
        x = 0
        while x < len(to_replace)-1:
            word1[to_replace[x]],word1[to_replace[x+1]] = word1[to_replace[x+1]],word1[to_replace[x]]
            x += 2
            counter += 1
        return counter
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            word1[i] = word2[i]
            counter +=1
    for i in word2:
        if i not in word1 or (i in word1 and word2.count(i) > word1.count(i)):
            if len(word2) <= len(word1):
                break
            word1.append(i)
            counter += 1

    print(word1)
    return counter
    

print(edit_distance("horse", "ros"))
print(edit_distance("intention", "execution"))
print(edit_distance("kitten", "sitting"))


