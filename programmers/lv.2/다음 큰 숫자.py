def solution(n):
    answer = 0
    c = n+1
    while(1):
        bin_n = bin(n)
        bin_c = bin(c)
        if bin_n.count('1') == bin_c.count('1'):
            answer = c
            break
        else:
            c = c + 1
    return answer

print(solution(76))
