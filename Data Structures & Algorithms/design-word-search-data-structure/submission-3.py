class DictNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.dummy = DictNode()

    def addWord(self, word: str) -> None:
        temp = self.dummy
        for char in word:
            if char not in temp.children:
                temp.children[char] = DictNode()
            temp = temp.children[char]
        
        temp.end = True

    def search(self, word: str) -> bool:

        def dfs(node, i):
            if i >= len(word):
                return node.end

            if word[i] != "." and word[i] not in node.children:
                return False
            if word[i] == ".":
                for child in node.children:
                    if dfs(node.children[child], i+1):
                        return True
                return False
            else:
                return dfs(node.children[word[i]], i+1)
        
        return dfs(self.dummy, 0)
