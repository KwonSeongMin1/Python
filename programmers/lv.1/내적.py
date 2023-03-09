def solution(a, b):
    answer = 0
    for x,y in zip(a,b):
        answer = answer + x*y
        
    return answer