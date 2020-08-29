def solution(cookie):
    answer = 0
    mid = 0
    while mid < len(cookie)-1:
        l, r = mid, mid + 1
        lres, rres = cookie[l], cookie[r]
        while l > 0 and r < len(cookie):
            if lres > rres:
                rres += cookie[r]
                r += 1
            elif lres < rres:
                lres += cookie[l]
                l -= 1
            else:
                if answer < lres:
                    answer = lres
                r += 1
                l -= 1
        mid += 1
    return answer
print(solution([1,1,2,3]))