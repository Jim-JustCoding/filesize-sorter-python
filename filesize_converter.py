# b = bytes
def calcKB(b):
    return round(b / 1024, 2)

def calcMB(b):
    return round(b / 1048576, 2)

def calcGB(b):
    return round(b / 1073741824, 2)


def calcSize(bytes):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024:
            return "%3.2f %s" % (bytes, x)
        bytes /= 1024.0