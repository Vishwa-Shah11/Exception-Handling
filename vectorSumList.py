P = [1,2,3]
Q = [4,5,6]

#Type 1
R = [ ]
for x, y in zip(P, Q):
    R.append(x + y)

#Type 2
R1 = [P[i] + Q[i] for i in range(len(P))]


#Printing for bith type
print(R)
print(R1)