def solution(s):
    s = list(s)
    print(s)
    upper = 1
    for i in range(len(s)):
        
        # 대소문자 변경
        if upper:
            s[i] = s[i].upper()
        else:
            s[i] = s[i].lower()
            
        # 대소문자 바꿀지 판별하는 파트
        if s[i] == " ":
            upper = 1
        else:
            upper = 0

    return ''.join(s)

print(solution("  asdf  asdf"))