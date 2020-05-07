def fileConverter(file):
    isStringEnd = False
    s = ""
    n = ""
    for i, v in enumerate(file):
        if isStringEnd == False:
            if v.isnumeric():
                # n += v
                isStringEnd = True
                s = file[:i].lower()
        if isStringEnd == True:
            if not v.isnumeric():
                break
            n+=v    
    return (s, int(n))
            
def solution(files):
    files.sort(key = lambda x: fileConverter(x))
    return files