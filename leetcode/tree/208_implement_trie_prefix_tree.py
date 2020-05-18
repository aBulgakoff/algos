def iterate_trie(root: dict, data: str) -> dict:
    node = root
    for symbol in data:
        node = node[symbol]
    return node


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        word = word + '.'
        node = self.root
        for symbol in word:
            if symbol not in node:
                node[symbol] = {}
            node = node[symbol]

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        try:
            node = iterate_trie(self.root, word)
        except KeyError:
            return False
        return '.' in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        try:
            iterate_trie(self.root, prefix)
        except KeyError:
            return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
from collections import defaultdict
from functools import reduce


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = lambda: defaultdict(self.trie)
        self.root = self.trie()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """

        reduce(dict.__getitem__, word, self.root)['.'] = word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for ch in word:
            if ch in node:
                node = node[ch]
            else:
                return False
        return node.get('.') == word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for ch in prefix:
            if ch in node:
                node = node[ch]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
