class Node:
    def __init__(self):
        self.child = {}
        self.word_end = False


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        temp = self.root

        for i in word:
            if i not in temp.child:
                temp.child[i] = Node()
            
            temp = temp.child[i]
        
        temp.word_end = True

    def search(self, word: str) -> bool:
        temp = self.root

        for i in word:
            if i not in temp.child:
                return False
            
            temp = temp.child[i]
        
        return temp.word_end

    def startsWith(self, prefix: str) -> bool:
        temp = self.root

        for i in prefix:
            if i not in temp.child:
                return False
            
            temp = temp.child[i]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)