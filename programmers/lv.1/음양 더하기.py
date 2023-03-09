def solution(absolutes, signs):
    answer = 0
    for ab,s in zip(absolutes,signs):
        if s:   #양
            answer = answer + ab
        else:   #음
            answer = answer - ab
    return answer