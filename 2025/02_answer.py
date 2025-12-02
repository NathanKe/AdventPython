from math import sqrt

inRanges = open('02_input').read().split(',')


def isSimpleValid(numStr):
    slen = len(numStr)
    if slen % 2 != 0:
        return False
    left = numStr[:slen//2]
    right = numStr[slen//2:]
    return left == right


def chunkify(numStr, chunkLen):
    return [numStr[i:i+chunkLen] for i in range(0,len(numStr),chunkLen)]


def isComplexValid(numStr):
    for chk in range(1,int(sqrt(len(numStr)))+3):
        if len(numStr)%chk == 0:
            cChunks = chunkify(numStr,chk)
            if len(cChunks) >= 2 and len(set(cChunks))==1:
                return True
    return False


def validSum(rangeStr):
    low, high = rangeStr.split('-')
    vs = 0
    vsc = 0
    for num in range(int(low), int(high)+1):
        if isSimpleValid(str(num)):
            vs += num
        if isComplexValid(str(num)):
            vsc += num
    return vs, vsc


resArr = [validSum(x) for x in inRanges]

print(sum(map(lambda x: x[0], resArr)))
print(sum(map(lambda x: x[1], resArr)))
