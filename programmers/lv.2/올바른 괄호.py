def solution(s):
    left = 0
    right = 0
    ans = True
    
    for stack in s:
        if stack == "(":
            left = left + 1
        if stack == ")":
            right = right + 1
        if left < right:
            ans = False
            break
        

    if left != right:
        ans = False
    return ans
solution("()()")