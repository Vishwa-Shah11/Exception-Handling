M = [[1,2,3], [3,4,5], [5,6,7]]

#Type 1
rsum = [sum(row) for row in M]

#Type 2
m, n = len(M), len(M[0])
rsums = []
for i in range(m):
    val = 0
    for j in range(n):
        val += M[i][j]
    rsums.append(val)

#Type 3
rsumss = [ ]
for row in M:
    rsumss.append(sum(row))


#Printing for all 3 types
print(rsum)
print(rsums)
print(rsumss)