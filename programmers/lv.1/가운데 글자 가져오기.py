def solution(s):
    answer = ""
    if len(s) % 2 == 0: #짝
        answer = s[len(s)//2-1] + s[len(s)//2]
    else:   #홀
        answer = s[len(s)//2]
    return answer