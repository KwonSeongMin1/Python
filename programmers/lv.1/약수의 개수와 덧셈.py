def solution(left, right):
    answer = 0
    for i in range(left,right+1,1):
        count = 0  #약수 개수
        for j in range(1,i+1,1):
            if i%j==0:
                count = count + 1
                #약수 개수 판별기
        if count%2 == 0:
            answer = answer + i
        else:
            answer = answer - i
    return answer