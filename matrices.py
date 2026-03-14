import random
import math

matrixB = [[4,5,6],[7,8,9],[10,11,12]]
matrixA = [[1,2,3], [1,2,3], [1,2,3]]
matrixC = [[0,0,0], [0,0,0], [0,0,0]]

def print_matrix(list):
    for i in range(0,3):
        for j in range(0,3):
            print (list[i][j],end=" ")
        print("\n")
#print_matrix()

def calc_matrix(symbol):
    global matrixC
    if symbol == "+":
        for i in range(0,3):
            for j in range(0,3):
                matrixC[i][j] = matrixA[i][j]+matrixB[i][j]
    elif symbol == "-":
        for i in range(0,3):
            for j in range(0,3):
                matrixC[i][j] = matrixA[i][j]-matrixB[i][j]
    elif symbol == "x":
        for i in range(0,3):
            for j in range(0,3):
                matrixC[i][j] = matrixA[i][j]*matrixB[i][j]
    elif symbol == "/":
        for i in range(0,3):
            for j in range(0,3):
                matrixC[i][j] = matrixA[i][j]/matrixB[i][j]

    

calc_matrix("-")
print_matrix(matrixC)