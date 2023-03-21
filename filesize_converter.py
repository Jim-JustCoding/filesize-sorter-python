# b = bytes
def calcKB(b):
    return b / 1024

def calcMB(b):
    return b / 1048576

def calcGB(b):
    return b / 1073741824

def calcSize(bytes):
    if bytes < 1048576:
        result = str(round(calcKB(bytes), 2)) + ' KB'
        return result
    if bytes < 1073741824:
        result = str(round(calcMB(bytes), 2)) + ' MB'
        return result
    else:
        result = str(round(calcGB(bytes), 2)) + ' GB'
        return result
