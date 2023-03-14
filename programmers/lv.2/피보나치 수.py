def solution(n):
    a1 = 0
    a2 = 1
    a3 = 0
    for _ in range(n-1):
        a3 = a1 + a2
        a1 = a2
        a2 = a3
    return a3