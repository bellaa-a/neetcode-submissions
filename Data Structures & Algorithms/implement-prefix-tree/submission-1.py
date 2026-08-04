class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.dummy = TrieNode()

    def insert(self, word: str) -> None:
        temp = self.dummy
        for i in range(len(word)):
            if word[i] in temp.children.keys():
                temp = temp.children[word[i]]
            else:
                temp.children[word[i]] = TrieNode()
                temp = temp.children[word[i]]
            if i == len(word)-1:
                temp.end = True

    def search(self, word: str) -> bool:
        temp = self.dummy
        for i in range(len(word)):
            if word[i] in temp.children.keys():
                temp = temp.children[word[i]]
            else:
                return False
            
            if i == len(word)-1 and temp.end != True:
                return False
        
        return True

    def startsWith(self, prefix: str) -> bool:
        temp = self.dummy
        for i in range(len(prefix)):
            if prefix[i] in temp.children.keys():
                temp = temp.children[prefix[i]]
            else:
                return False
        
        return True
        
        