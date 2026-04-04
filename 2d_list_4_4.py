matrix = []
value = 1
for i in range(4):
    row = []
    for j in range(4):
        row.append(value)
        value += 1
    matrix.append(row)

print("2D List (4x4):")
for i in range(4):
    for j in range(4):
        print(matrix[i][j], end=" ")
    print()
