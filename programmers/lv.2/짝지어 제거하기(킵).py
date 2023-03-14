def solution(s):
    answer = []
    i = 0
    while(1):
        answer.append(s[i])
        if len(s) == 1:
            continue
        if s[i] == s[i+1]:
            del s[i:i+2]
            
        if i == len(s)-1 or len(s) == 0:
            break 
    if len(s):
        answer = 0
        

    return answer
solution("baabaa")
#https://school.programmers.co.kr/learn/courses/30/lessons/12973
#너무 오래걸려서 일단 킵