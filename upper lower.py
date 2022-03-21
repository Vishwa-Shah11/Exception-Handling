L = ['Vishwa', 'heet', 'Shah']


#List that start with lower case
P = [name for name in L if 'a' <= name[0] <= 'z']


#List that starts with upper case---Type 1
P1 = [name for name in L if 'A' <= name[0] <= 'Z']


#List that starts with upper case---Type 2
P2 = [ ]
for name in L:
    if 'A' <= name[0] <= 'Z':
        P2.append(name)

#Printing for all three
print(P)
print(P1)
print(P2)