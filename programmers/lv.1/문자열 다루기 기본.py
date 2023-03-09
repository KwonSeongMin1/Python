def solution(s):
    answer = True
    try:
        if len(s) == 4 or len(s) == 6:
            s = int(s)
        else:
            answer = False
    except:
        answer = False
    return answer