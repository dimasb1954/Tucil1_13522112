import time

def find(nbuff, mWidth, mHeight, matrix, nSeq, arrSeq, arrPoint):
    start = time.time()

    buff = nbuff

    coorAll = []

    coorRoot = []

    for i in range (0, mWidth):
        coorRoot += [[[0, i]]]

    coorAll += coorRoot

    for i in range (1, buff):
        coorNew = []
        if i % 2 == 1:
            for coor in coorRoot :
                path = []
                path += coor
                abs, oor = coor[len(coor)-1][0], coor[len(coor)-1][1]
                for j in range (0, mHeight):
                    path += ([[j, oor]])
                    coorNew.append(path)
                    path = path[:-1]

        if i % 2 == 0:
            for coor in coorRoot :
                path = []
                path += coor
                abs, oor = coor[len(coor)-1][0], coor[len(coor)-1][1]
                for j in range (0, mWidth):
                    path += ([[abs, j]])
                    coorNew.append(path)
                    path = path[:-1]

        coorAll += coorNew
        coorRoot = coorNew

    remove = []

    toRemove = 0

    for seq in coorAll:
        total = 0
        for coor in seq:
            for i in range (0, len(seq)):
                if coor == seq[i]:
                    total += 1
        if total > len(seq):
            remove.append(toRemove)
        toRemove += 1

    for j in range (len(remove)-1, -1, -1):
        coorAll.pop(remove[j])

    pointAll = [0] * len(coorAll)

    for i in range (0, len(coorAll)):
        for j in range (0, nSeq):
            if (len(coorAll[i]) >= len(arrSeq[j])):
                for k in range (0, len(coorAll[i]) - len(arrSeq[j]) + 1):
                    status = 0
                    for l in range (0, len(arrSeq[j])):
                        if (matrix[coorAll[i][k+l][0]][coorAll[i][k+l][1]] == arrSeq[j][l]):
                            status += 1
                    if (status == len(arrSeq[j])):
                        pointAll[i] += arrPoint[j]

    max = 0
    loc = 0
    tokenRes = []
    coorRes = []

    for i in range (0, len(pointAll)):
        if pointAll[i] > max:
            max = pointAll[i]
            loc = i

    step = len(coorAll[loc])

    for i in range (0, step):
        tokenRes.append(matrix[coorAll[loc][i][0]][coorAll[loc][i][1]])
        coorRes.append(coorAll[loc][i])
        coorRes[i][0], coorRes[i][1] = coorRes[i][1]+1,coorRes[i][0]+1

    end = time.time()
    elapsedTime = end - start

    return max, tokenRes, coorRes, elapsedTime