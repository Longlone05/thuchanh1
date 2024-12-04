from random import randrange

matrix = []
row = int(input("Nhập số dòng: "))
column = int(input("Nhập số cột: "))

zero_row = set()
zero_column = set()
sokhong = False  


for i in range(row):
    onerow = []  # Tạo một dòng
    for j in range(column):
        onerow.append(randrange(0, 21))  # Số ngẫu nhiên từ 0 đến 20
    matrix.append(onerow)


print("Ma trận ban đầu:")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end="\t")
    print()

for i in range(row):
    for j in range(column):
        if matrix[i][j] == 0:
            sokhong = True  
            zero_row.add(i)
            zero_column.add(j)


if sokhong:  
    
    for r in zero_row:
        for j in range(column):
            matrix[r][j] = 0

    for c in zero_column:
        for i in range(row):
            matrix[i][c] = 0


    print("\nMa trận sau khi đặt các hàng và cột có số 0 thành 0:")
    for r in matrix:
        print(r)
else:
    print("\nKhông có số 0 trong ma trận.")

