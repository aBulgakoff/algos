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

