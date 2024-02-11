import os

def getDirectory():
    # Mengembalikan directory saat ini
    return os.path.dirname(os.path.realpath(__file__))

def scanFile(nameFile):
    # Membaca File
    currentDir = getDirectory()
    f = open(os.path.join(currentDir, f"TEST", f"{nameFile}"), 'r')
    arr = f.readlines()
    f.close()

    return arr

def getFromFile(entry):
    # Mengembalikan isi dari file dalam variabel variabel
    buff = int(entry[0])
    mWidth, mHeight = entry[1][0], entry[1][2]
    mWidth = int(mWidth)
    mHeight = int(mHeight)

    matrix = []
    for i in range (2, 2+mHeight) :
        element = [None] * mWidth
        element = entry[i].split()
        matrix.append(element)

    nSeq = int(entry[2+mHeight])

    arrSeq = []
    for i in range (2+mHeight+1, 2+mHeight+2*nSeq+1, 2):
        element = [None] * mWidth
        element = entry[i].split()
        arrSeq.append(element)

    arrPoint = []
    for i in range (2+mHeight+2, 2+mHeight+2*nSeq+1, 2):
        point = int(entry[i])
        arrPoint.append(point)

    return buff, mWidth, mHeight, matrix, nSeq, arrSeq, arrPoint

def create_text_file_in_folder(folder_path, nameFile, max, tokenRes, coorRes, elapsedTime):

    file_path = os.path.join(folder_path, nameFile)

    with open(file_path, 'w') as file:
        max = str(max)
        file.write(max + "\n")
        token = tokenRes[0]
        for i in range (1, len(tokenRes)):
            token += " " + tokenRes[i]
        file.write(token)
        for i in range (0, len(coorRes)):
            coor = str(coorRes[i][0]) + ", " + str(coorRes[i][1])
            file.write("\n" + coor)
        elapsedTime = str(elapsedTime) + "s"
        file.write("\n" + elapsedTime)



