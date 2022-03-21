P = input().split(',')
L = [ ]
for word in P:
    if 'e' not in word:
        L.append(word)
print(L)

L = [word for word in input().split(',') if 'e' not in word]
print(L)

print([word for word in input().split(',') if 'e' not in word])