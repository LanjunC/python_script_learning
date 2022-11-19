import os
import sys

fileMap = {}
whiteList = ['.py', '.sh', '.cpp', '.h', '.c']
defaultBasePath = "./"


def init():
    for ext in whiteList:
        fileMap[ext] = []


def getFile(basePath):
    global fileMap
    for dirpath, dirnames, filenames in os.walk(basePath):
        for filename in filenames:
            ext = "." + filename.split(".")[-1]  # like ".py"
            if ext in whiteList:
                fileMap[ext].append(os.path.join(dirpath, filename))


def countLine(filename):
    count = 0
    for fileLine in open(filename, 'rb').readlines():
        if not fileLine.isspace():
            count += 1
    return count


if __name__ == '__main__':
    init()
    basePath = defaultBasePath
    if len(sys.argv) == 2:
        basePath = sys.argv[1]
    getFile(basePath)

    totalCount = 0
    print("type".ljust(15), "count".rjust(15), sep="")
    print("=" * 30, sep="")
    for ext, flist in fileMap.items():
        if len(flist) == 0:
            continue
        count = 0
        for file in flist:
            count += countLine(file)
        print(ext.ljust(15), format(count, ",").rjust(15), sep="")
        totalCount += count
    print("=" * 30, sep="")
    print("(all)".ljust(15), format(totalCount, ",").rjust(15), sep="")
