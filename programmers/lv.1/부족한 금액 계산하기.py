def solution(price, money, count):
    s = 0
    for i in range(1,count+1,1):
        s = s + price * i

    answer = s - money
    if answer < 0:
        answer = 0
    return answer


print(solution(3,20,4))