# anta, tica 를 제외한 글자 갯수를 확인한다.
# # K개의 글자에서 anta, tica의 글자를 뺀다.
# # 만약 음수가 된다면 모든 글자를 읽을 수 없다.
# # 모든 글자를 set에 넣고 거기서 뺀 글자 수 만큼 조합을 짠다.
# # 남는 글자수가 뽑아야되는 글자 수보다 작게 되면 모든 글자를 읽을 수 있다.
def back(depth, n):
    global result
    if len(selectch) == n+5:
        res = 0
        for word in words:
            res += 1
            for ch in word:
                if not selectch.get(ch):
                    res -= 1
                    break

        result = max(result, res)
        return

    for i in range(depth, len(chars)):
        selectch[chars[i]] = True
        back(i+1, n)
        del selectch[chars[i]]

N, K = map(int, input().split())
chars = set()
words = []
selectch = dict()
for ch in 'antatica':
    selectch[ch] = True
for _ in range(N):
    tmp = input()
    ttmp = list(set(list(tmp[4:-4])))
    words.append(ttmp)
    for ch in tmp[4:-4]:
        if not selectch.get(ch):
            chars.add(ch)
result = 0
k = K - len(selectch)
if k < 0:
    print(0)
elif k > 0 and k > len(chars):
    print(N)
else:
    chars = list(chars)
    back(0, k)
    print(result)

