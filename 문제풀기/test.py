class Node:
    def __init__(self, key):
        self.key = key
        self.child = dict()

class Trie:

    def __init__(self):
        self.head = Node(None)

    def insert(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur.child:
                cur.child[ch] = Node(ch)
            cur = cur.child[ch]
        cur.child['*'] = True

    def search(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur.child:
                return False
            cur = cur.child[ch]

        if '*' in cur.child:
            return True
        else:
            return False
trie = Trie()
trie.insert('aabb')
trie.insert('aacc')
print(trie.search('aabb'))
print(trie.search('aa'))