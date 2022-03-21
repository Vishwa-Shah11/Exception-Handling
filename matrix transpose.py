M = [[1,2,3], [3,4,5], [5,6,7]]

#Type 1
M_t = [[M[j][i] for j in range(len(M))] for i in range(len(M))]


#Type 2
M1_t = [ ]
n = len(M)
for i in range(n):
    M1_t.append([ ])
    for j in range(n):
        M1_t[-1].append(M[j][i])


#Printing for both types
print(M_t)
print(M1_t)