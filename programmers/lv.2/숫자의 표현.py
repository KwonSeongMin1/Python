def solution(n):
    answer = 0
    for i in range(1,n+1):
        gg = 0
        for j in range(i,n+1):
            gg = gg + j
            if gg == n:
                answer = answer + 1
                break
            if gg > n:
                break
    return answer

print(solution(15))