T = int(input())

for tc in range(1, T+1):
    N, M, K, A, B = map(int, input().split())
    reception = list(map(int, input().split()))
    repair = list(map(int, input().split()))
    person = list(map(int, input().split()))
    visit = [0] * K
    reception_visit = [0] * N
    repair_visit = [0] * M
    waiting = []
    time = 0
    repair_waiting = []
    track = {x:[] for x in range(K)}

    while sum([len(x) for x in track.values()]) < 2 * K:
        for i in range(M): # 수리 마치고 나가는 사람
            if repair_visit[i] != 0 and repair_visit[i][1] == time:
                repair_visit[i] = 0


        for i in range(N): # 접수 끝내고 대기 장소에 넣기
            if reception_visit[i] != 0 and reception_visit[i][1] == time:
                repair_waiting.append(reception_visit[i][0])
                reception_visit[i] = 0

        if repair_waiting:
            cnt = 0
            for p in repair_waiting:
                for i in range(M):
                    if not repair_visit[i]:
                        cnt += 1
                        track[p].append(i)
                        repair_visit[i] = (p, time + repair[i])
                        break

            for _ in range(cnt): repair_waiting.pop(0)

        for i in range(K):
            if not visit[i] and person[i] == time:
                waiting.append(i)
                visit[i] = 1
        if waiting:
            cnt = 0
            for p in waiting:
                for i in range(N):
                    if not reception_visit[i]:
                        reception_visit[i] = (p, time + reception[i])
                        track[p].append(i)
                        cnt += 1
                        break
            for _ in range(cnt): waiting.pop(0)
        time += 1
    result = 0
    for key, val in track.items():
        if val == [A-1, B-1]:
            result += (key+1)
    if not result:
        print('#{} -1'.format(tc))
    else:
   		print('#{}'.format(tc), result)



