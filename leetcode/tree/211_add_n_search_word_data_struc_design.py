from collections import defaultdict
from functools import reduce

Trie = lambda: defaultdict(Trie)


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        reduce(dict.__getitem__, word, self.trie)['word'] = word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        stack = [[self.trie]]
        ix = 0
        while ix < len(word) and stack and stack[-1]:
            nodes = stack.pop()
            stack.append(next_nodes := [])
            if word[ix] == '.':
                next_nodes.extend(node[k] for node in nodes for k in node if k != 'word')
            else:
                next_nodes.extend(filter(None, map(lambda node: node.get(word[ix]), nodes)))
            if not next_nodes:
                break
            ix += 1
        return ix == len(word) and any('word' in node for node in stack[-1])

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
