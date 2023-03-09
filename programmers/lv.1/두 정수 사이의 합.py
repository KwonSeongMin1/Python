def solution(a, b):
    answer = 0
    if a>b:
        tmp = a
        a = b
        b = tmp
        #오름차순 정렬
    for i in range(a,b+1,1):
        answer = answer + i
    return answer