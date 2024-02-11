import random

def getFromCom(nToken, arrToken, mWidth, mHeight, nSeq, maxSeq):
    # Mengembalikan matrix, sekuen, dan point dari sekuen berdasarkan masukan
    matrix = []
    for _ in range (0, mHeight) :
        element = []
        for i in range (0, mWidth) :
            n = random.randrange(0, nToken)
            token = arrToken[n]
            element.append(token)
        matrix.append(element)

    arrSeq = []
    for _ in range (0, nSeq):
        element = []
        n = random.randrange(2,maxSeq+1)
        for _ in range (0, n):
            m = random.randrange(0, nToken)
            token = arrToken[m]
            element.append(token)
        arrSeq.append(element)

    arrPoint = []
    for _ in range (0, nSeq):
        n = random.randrange(5, 10*nSeq, 5)
        arrPoint.append(n)

    return matrix, arrSeq, arrPoint