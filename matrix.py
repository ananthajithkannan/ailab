

r1 = int(input("Enter number of rows for first matrix: "))
c1 = int(input("Enter number of columns for first matrix: "))

print("Enter elements of first matrix (row-wise):")
A = []
for i in range(r1):
    row = list(map(int, input().split()))
    A.append(row)

 
r2 = int(input("Enter number of rows for second matrix: "))
c2 = int(input("Enter number of columns for second matrix: "))

 
print("Enter elements of second matrix (row-wise):")
B = []
for i in range(r2):
    row = list(map(int, input().split()))
    B.append(row)

 
print("\nMatrix A:")
for row in A:
    print(row)
print("\nMatrix B:")
for row in B:
    print(row)

 
if r1 == r2 and c1 == c2:
    C = [[A[i][j] + B[i][j] for j in range(c1)] for i in range(r1)]
    print("\nMatrix Addition Result:")
    for row in C:
        print(row)
else:
    print("\nMatrix addition not possible.")

 
if r1 == r2 and c1 == c2:
    D = [[A[i][j] - B[i][j] for j in range(c1)] for i in range(r1)]
    print("\nMatrix Subtraction Result:")
    for row in D:
        print(row)
else:
    print("\nMatrix subtraction not possible.")

 
if c1 == r2:
    result = [[0 for _ in range(c2)] for _ in range(r1)]
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += A[i][k] * B[k][j]
    print("\nMatrix Multiplication Result:")
    for row in result:
        print(row)
else:
    print("\nMatrix multiplication not possible.")