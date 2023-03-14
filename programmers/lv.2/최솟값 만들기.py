def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    
    answer = 0
    for _ in range(len(A)):
        answer = answer + A[0] * B[0]
        A.pop(0)
        B.pop(0)
                
    return answer
solution([1,2,3],[4,5,6])