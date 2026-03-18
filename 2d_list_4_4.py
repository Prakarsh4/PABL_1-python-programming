# Create a 4x4 2D list with values 1 to 16
matrix = []
value = 1
for i in range(4):
    row = []
    for j in range(4):
        row.append(value)
        value += 1
    matrix.append(row)

# Print all elements using loops
print("2D List (4x4):")
for i in range(4):
    for j in range(4):
        print(matrix[i][j], end=" ")
    print()
