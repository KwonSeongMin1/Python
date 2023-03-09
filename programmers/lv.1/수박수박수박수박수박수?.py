def solution(n):
    answer = ''
    for w in range(1,n+1,1):
        if w%2:
            answer = answer + "수"
        else:
            answer = answer + "박"
    return answer