def solution(participant, completion):
    answer = ''
    my_dict = {x:0 for x in participant}
    for i in participant:
        my_dict[i] += 1
    for j in completion:
        my_dict[j] -= 1
    for key, value in my_dict.items():
        if value > 0:
            answer += key
    return answer


print(solution(['leo', 'kiki', 'eden'], ['eden', 'kiki']))