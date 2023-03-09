def solution(arr, divisor):
    arr.sort()  #오름차순 정렬
    answer = []
    flag = True    #값 들어가는지 판별
    
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
            flag = False
    
    if flag:    #값 들어간거 없으면
        answer.append(-1)
    return answer