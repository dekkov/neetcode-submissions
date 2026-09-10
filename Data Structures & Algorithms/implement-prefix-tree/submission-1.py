class Node:

    def __init__(self):
        self.children = {} # character:Node 
        self.isWord = False

"""
Prefix Tree will have Nodes

Nodes will contain a hashmap to store the next possible node
Each node will be a character 
The last character node of a word should have isWord = True

Each node should also have a list to return for the starts with
"""
class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Go through each of the character in the word
        -> add them as node
        """
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        
        cur.isWord = True

    def search(self, word: str) -> bool:
        """
        Keep going through each character of the word 
            If a char is not found in the current path
                return False
            Otherwise
                keep traversing
            check if that last char has isWord = true
        """

        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            else:
                cur = cur.children[c]
        
        return cur.isWord

    def startsWith(self, prefix: str) -> bool:
        """
        Keep iterate thru the prefix
        at the last char of prefix we return that char's swList
        """

        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            else:
                cur = cur.children[c]
        
        return True
        
        