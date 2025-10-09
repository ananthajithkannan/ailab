def input_matrix(rows, cols): 
    print(f"Enter elements for a {rows}x{cols} matrix:") 
    matrix = [] 
    for i in range(rows): 
        row = list(map(int, input(f"Enter elements of row {i+1} (space-separated): ").split())) 
        matrix.append(row) 
    return matrix 
 
def add_matrices(a, b): 
    result = [] 
    for i in range(len(a)): 
        row = [] 
        for j in range(len(a[0])): 
            row.append(a[i][j] + b[i][j]) 
        result.append(row) 
    return result 
 
def sub_matrices(a, b): 
    result = [] 
    for i in range(len(a)): 
        row = [] 
        for j in range(len(a[0])): 
            row.append(a[i][j] - b[i][j]) 
        result.append(row) 
    return result 
 
r1 = int(input("Enter rows of first matrix: ")) 
c1 = int(input("Enter columns of first matrix: ")) 
a = input_matrix(r1, c1) 
 
r2 = int(input("Enter rows of second matrix: ")) 
c2 = int(input("Enter columns of second matrix: ")) 
b = input_matrix(r2, c2) 
print("\nMatrix A:") 
print(a) 
print("\nMatrix B:") 
print(b) 
if r1 == r2 and c1 == c2: 
    print("\nMatrix Addition:") 
    for row in add_matrices(a, b): 
        print(row) 
    print("\nMatrix Subtraction:") 
    for row in sub_matrices(a, b): 
        print(row) 
else: 
    print("\nAddition and subtraction not possible") 