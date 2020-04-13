class Node:
    def __init__(self, key):
        self.key = key
        self.child = dict()
        self.remain = dict()
class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, word):
        cur = self.head
        cnt = 0
        for ch in word:
            if ch not in cur.child:
                cur.child[ch] = Node(ch)
            if not cur.remain.get(len(word) - cnt):
                cur.remain[len(word) - cnt] = 0
            cur.remain[len(word) - cnt] += 1

            cur = cur.child[ch]
            cnt += 1
        cur.child['*'] = True



    def search(self, word):
        cur = self.head
        for idx, ch in enumerate(word):
            if cur.child.get(ch):
                cur = cur.child[ch]
            elif ch == '?':
                if cur.remain.get(len(word) - idx):
                    return cur.remain.get(len(word) - idx)
                else:
                    return False
            else:
                return False
        if '*' in cur.child:
            return True


trie = Trie()
inv_trie = Trie()
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
answer = [0] * len(queries)
for word in words:
    trie.insert(word)
    inv_trie.insert(word[::-1])
for idx, query in enumerate(queries):
    if query[0] == '?':
        tmp = inv_trie.search(query[::-1])
    else:
        tmp = trie.search(query)
    if tmp:
        answer[idx] += tmp
print(answer)