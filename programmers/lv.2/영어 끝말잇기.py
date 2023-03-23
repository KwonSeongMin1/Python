def solution(n, words):
    last_word = words[0][0]
    play_count = 1  # 턴
    wrong_player = 0    # 틀린 사람
    complete_game = 1   # -완- 체크
    used_word = []
    
    for w in words:
        used_word.append(w)
        wrong_player = wrong_player + 1
        # 턴제 체크
        if wrong_player > n:
            play_count = play_count + 1
            wrong_player = 1  
        
        # 판별기
        if last_word != w[0] or used_word.count(w) > 1:
            complete_game = 0 
            break
        else:
            last_word = w[-1]
        
    # -완- 게임 체크
    if complete_game:
        play_count = 0 
        wrong_player = 0
        
    return [wrong_player,play_count]

solution(2,["hello", "one", "even", "never", "now", "world", "draw"])