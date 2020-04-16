from collections import defaultdict
from functools import reduce
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


class Solution2(object):
    def replaceWords(self, roots: List[str], sentence: str) -> str:
        Trie = lambda: defaultdict(Trie)
        trie = Trie()  # initialize empty default dict which generates trie nods

        for root in roots:  # when getting letters from Trie default dict creates nodes for each letter
            reduce(dict.__getitem__, root, trie)['.'] = root  # in last node create marker with value of word

        def get_root(word):
            node = trie
            for ch in word:
                if '.' in node or ch not in node:
                    break
                node = node[ch]
            return node.get('.', word)  # return node if is word not prefix else - original word

        return ' '.join(map(get_root, sentence.split()))  # collect new string with roots if found or words
