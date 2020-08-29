from collections import deque


class Node():
    def __init__(self, ch):
        self.ch = ch
        self.child = dict()
        self.count = 1


class Trie():
    def __init__(self):
        self.head = Node(None)
        self.result = 0

    def put(self, word):
        cur = self.head
        for ch in word:
            if ch in cur.child:
                cur.count += 1
                cur = cur.child[ch]
            else:
                tmp = Node(ch)
                cur.child[ch] = tmp
                cur = tmp
        cur.child['.'] = None

    def find(self):
        stack = deque([(self.head, 0)])
        while stack:
            node, res = stack.popleft()
            if len(node.child) == 1 and node.count == 1:
                self.result += res
                continue
            print(node.ch, node.count, node.child, res)
            for key in node.child:
                if key == '.':
                    self.result += res
                else:
                    stack.append((node.child[key], res + 1))


def solution(words):
    trie = Trie()
    for word in words:
        trie.put(word)
    trie.find()
    return trie.result
solution(['word','war','warrior','world'])