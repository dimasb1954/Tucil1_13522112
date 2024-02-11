from readFile import *
from readCom import *
from bruteforce import *

print("-- BREACH PROTOCOL --")

statusSelect = False

while statusSelect == False:
    print("Select input (1/2) =")
    print("1. File input")
    print("2. Manual input")
    select = int(input("==> "))
    if select == 1:
        statusSelect = True
    elif select == 2:
        statusSelect = True
    else:
        print("Please type correctly")

if select == 1:
    nameFile = input("File = ")
    file = scanFile(nameFile)
    buff, mWidth, mHeight, matrix, nSeq, arrSeq, arrPoint = getFromFile(file)
    max, tokenRes, coorRes, elapsedTime = find(buff, mWidth, mHeight, matrix, nSeq, arrSeq, arrPoint)

elif select == 2:
    nToken = int(input())
    arrToken = input().split()
    buff = int(input())
    mWidth, mHeight = input().split()
    mWidth = int(mWidth)
    mHeight = int(mHeight)
    nSeq = int(input())
    maxSeq = int(input())
    matrix, arrSeq, arrPoint = getFromCom(nToken, arrToken, mWidth, mHeight, nSeq, maxSeq)
    max, tokenRes, coorRes, elapsedTime = find(buff, mWidth, mHeight, matrix, nSeq, arrSeq, arrPoint)
    print()
    print("MATRIX")
    for i in range (0, mHeight):
        for j in range (0, mWidth):
            print(matrix[i][j], end=" ")
        print("\n")
    print("SEKUEN")
    for i in range (0, nSeq):
        for j in range (0, len(arrSeq[i])):
            print(arrSeq[i][j], end=" ")
        print()
        print(arrPoint[i])

print()
print(max)
for token in tokenRes :
    print(token, end=" ")
print("\n")
for coor in coorRes :
    print("{}, {}".format(coor[0],coor[1]))
print("\n{}s".format(elapsedTime))

statusSave = False

while statusSave == False:
    print("\nApakah ingin menyimpan solusi? (y/n)")
    save = str(input())
    if save == "y":
        statusSave = True
        folder_path = '../test'
        nameFile = input("File = ")
        create_text_file_in_folder(folder_path, nameFile, max, tokenRes, coorRes, elapsedTime)
        print("\nAnswer saved")
    elif save == "n":
        statusSave = True
    else:
        print("Please type correctly")