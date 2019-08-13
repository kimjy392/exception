def solution(answers):
    answer = []
    supo = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    count = [0, 0, 0]
    problem = [0, 0, 0]
    for i in range(3):
        problem[i] = len(answers) // len(supo[i]) + 1
        supo[i] = problem[i] * supo[i]

    for j in range(3):
        for k in range(len(answers)):
            if supo[j][k] == answers[k]:
                count[j] += 1
    

    


solution([1,2,3,4,5])