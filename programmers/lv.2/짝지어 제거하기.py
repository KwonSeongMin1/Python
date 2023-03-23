def solution(s):
    answer = []
    before_word = ""
    result = 1  
    
    for word in s:
        answer.append(word)
        # 앞에 있는 문자와 같은지 비교
        if before_word == word:
            # 같은거 2개 삭제 후
            del answer[-2:]
            # 만약 answer 비어있으면 [[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]
            if answer == []:
                before_word = ""
            else:
                before_word = answer[-1]
        else:
            before_word = word
            
    if answer == []:
        result = 1
    else:
        result = 0
    return result
print(solution("baabaa"))
#https://school.programmers.co.kr/learn/courses/30/lessons/12973