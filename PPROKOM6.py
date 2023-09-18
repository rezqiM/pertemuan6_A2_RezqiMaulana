#tugas 1
nilai = set([3,6,9,2,5,7])
extend = {1,4,8,10}
nilai.update(extend)
print(nilai)

#tugas 2
nilai = set([3,6,9,2,5,7])
extend = {1,4,8,10}

nilai.update(extend) #penambahan
print(nilai)

hapus = {1,3,4,5,7,8,10}
remove = nilai - hapus #menhapus angka 1,3,4,5,7,8,10
print(remove)

#tugas 3
A = {100, 7, 8}
B = {200, 4, 5}
C = {300, 2, 3}
D = {100, 200, 300}

irisan1 = A & D
irisan2 = B & D
irisan3 = C & D
irisan4 = A & B & C & D

print(irisan1)
print(irisan2)
print(irisan3)
print(irisan4)

#tugas 4
A = {100, 7, 8}
B = {200, 4, 5}
C = {300, 2, 3}
D = {100, 200, 300}

union1 = A | B
union2 = B | C
union3 = B | C | D
union4 = A | B | C | D

print(union1)
print(union2)
print(union3)
print(union4)

# #tugas 5
A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }
C = {}

# a. A symmetric difference B
# b. B symmetric difference A
# c. A symmetric difference C
# d. B symmetric difference C

print(A.symmetric_difference(B))
print(B.symmetric_difference(A))
print(A.symmetric_difference(C))
print(B.symmetric_difference(C))

#tugas 6
A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }
C = {}

# a. A difference B
# b. B difference A
# c. A difference C
# d. B difference C

print(A - B)
print(B - A)
print(A.difference(C))
print(B.difference(C))