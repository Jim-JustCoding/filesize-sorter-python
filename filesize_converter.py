# b = bytes
def calcKB(b):
    return b / 1024

def calcMB(b):
    return b / 1048576

def calcGB(b):
    return b / 1073741824

def calcSize(bytes):
    if bytes < 1048576:
        return calcKB(bytes)
    if bytes < 1073741824:
        return calcMB(bytes)
    else:
        return calcGB(bytes)
