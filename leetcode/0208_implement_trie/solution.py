#!/usr/bin/env python3
# https://leetcode.com/problems/implement-trie-prefix-tree/description/


class Trie:
    def __init__(self, prefix=""):
        self.prefix = prefix
        self.children = {}
        self.terminal = False

    def __repr__(self):
        return f"<Trie prefix={self.prefix},  term={self.terminal}>"

    def insert(self, word: str) -> None:
        node = self
        for c in word:
            node = node.children.setdefault(c, Trie(prefix=node.prefix + c))
        node.terminal = True

    def search(self, word: str) -> bool:
        node = self
        try:
            for c in word:
                node = node.children[c]
        except KeyError:
            return False
        return node.terminal

    def startsWith(self, prefix: str) -> bool:
        node = self
        try:
            for c in prefix:
                node = node.children[c]
        except KeyError:
            return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

t = Trie()
words = "code leet cat car catalog do done dot".split()
print(f"{words=}")
for word in words:
    t.insert(word)
print()
