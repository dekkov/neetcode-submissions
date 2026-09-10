class Node:
    def __init__(self):
        self.children = {}       # character -> Node
        self.possibles = set()   # remaining word lengths possible from here
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word):
        cur = self.root
        remaining = len(word)

        # Root can lead to words of this length
        cur.possibles.add(remaining)

        for c in word:
            remaining -= 1

            if c not in cur.children:
                cur.children[c] = Node()

            cur = cur.children[c]
            cur.possibles.add(remaining)

        cur.isWord = True

    def find(self, i, word, root):
        cur = root
        remaining = len(word) - i

        # Early pruning:
        # no word of the required remaining length exists here.
        if remaining not in cur.possibles:
            return False

        # We've consumed the entire search word.
        if i == len(word):
            return cur.isWord

        c = word[i]

        if c == ".":
            # Try every possible character.
            return any(
                self.find(i + 1, word, node)
                for node in cur.children.values()
            )

        # Normal character lookup.
        if c not in cur.children:
            return False

        return self.find(i + 1, word, cur.children[c])


class WordDictionary:
    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.add(word)

    def search(self, word: str) -> bool:
        return self.trie.find(0, word, self.trie.root)
