from typing import List


class Trie:
    def __init__(self, tries: List[str]):
        self.trie = {}
        for trie in tries:
            self.insert_word(trie)

    def insert_word(self, word):
        node = self.trie
        for ch in word:
            node = node.setdefault(ch, {})
        node['.'] = word

    def get_root(self, word):
        node = self.trie
        for ch in word:
            if '.' in node or ch not in node:
                return node
            node = node[ch]
        return node


class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        trie = Trie(dict)
        return ' '.join(trie.get_root(word).get('.', None)
                        or word
                        for word
                        in sentence.split())
