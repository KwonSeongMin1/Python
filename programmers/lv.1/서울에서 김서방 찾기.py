def solution(seoul):
    Kim = 0
    for find in seoul:
        if find == "Kim":
            break
        Kim = Kim + 1
    answer = "김서방은 %d에 있다"%Kim
    return answer