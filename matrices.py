import random
import math

matrixA = [[1,2,3],[4,5,6],[7,8,9]]
matrixB = [[4,5,6],[7,8,9],[10,11,12]]
matrixC = [[0,0,0],[0,0,0],[0,0,0]]

matrixT = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

def print_matrix(list):
    for i in range(len(list)):
        for j in range(len(list[0])):
            print(list[i][j], end=" ")
        print("\n")

def calc_matrix(symbol):
    global matrixC
    if symbol == "+":
        for i in range(0,3):
            for j in range(0,3):
                matrixC[i][j] = matrixA[i][j] + matrixB[i][j]
    elif symbol == "-":
        for i in range(0,3):
            for j in range(0,3):
                matrixC[i][j] = matrixA[i][j] - matrixB[i][j]
    elif symbol == "x":
        for i in range(0,3):
            for j in range(0,3):
                matrixC[i][j] = matrixA[i][j] * matrixB[i][j]
    elif symbol == "/":
        for i in range(0,3):
            for j in range(0,3):
                matrixC[i][j] = matrixA[i][j] / matrixB[i][j]

def find_max(matrix):
    max_val = matrix[0][0]
    max_row = 0
    max_col = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
                max_row = i
                max_col = j
    return max_val, max_row, max_col

def transpose_3x4(matrix):
    result = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(4):
            result[j][i] = matrix[i][j]
    return result

print("Matrix A:")
print_matrix(matrixA)

print("Matrix B:")
print_matrix(matrixB)

symbol = input("Enter operation (+, -, x, /): ")
calc_matrix(symbol)

print("Matrix C:")
print_matrix(matrixC)

maxA = find_max(matrixA)
print("Max of A:", maxA)

maxB = find_max(matrixB)
print("Max of B:", maxB)

maxC = find_max(matrixC)
print("Max of C:", maxC)


print("Transposed 4x3 Matrix:")
print_matrix(transpose_3x4(matrixT))
