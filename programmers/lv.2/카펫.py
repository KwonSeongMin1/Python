def solution(brown, yellow):
    
    answer = []
    carpet = brown + yellow
    for i in range(3,carpet):
        if carpet % i == 0:
            if carpet // i <= carpet // (carpet // i):
                answer.append(carpet // (carpet // i))
                answer.append(carpet // i)
                return answer
            
print(solution(18,6))