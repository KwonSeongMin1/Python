def solution(num):
    count = 0
    while(num!=1):
        if num%2:   #짝수
            num = num * 3
            num = num + 1
        else:   #홀수
            num = num / 2
        count = count + 1
        if count >= 500:    #500번 카운트되면?
            count = -1
            break
    return count