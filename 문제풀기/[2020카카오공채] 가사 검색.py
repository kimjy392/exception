def solution(words, queries):
    answer = [0] * len(queries)
    for idx, query in enumerate(queries):
        for word in words:
            if len(word) != len(query):
                continue
            flag = 0
            where = query.find('?')
            if where == -1:
                if word != query:
                    flag = 1
            elif where == 0:
                qidx = query.count('?')
                if word[qidx:] != query[qidx:]:
                    flag = 1
            elif where > 0:
                if word[:where] != query[:where]:
                    flag = 1
            if not flag:
                answer[idx] += 1
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro???"]))