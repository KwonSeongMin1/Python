def solution(s):
    pCount = 0
    yCount = 0
    result = True
    
    for w in s:
        if w == "p" or w == "P":
            pCount = pCount + 1
        if w == "y" or w == "Y":
            yCount = yCount + 1
    
    if pCount == yCount:
        result = True
    else:
        result = False
    
    return result