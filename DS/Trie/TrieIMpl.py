from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children=defaultdict(TrieNode)
        self.isEnd=False


class Trie:
    diff=0
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        temp=self.root
        for ch in word:
            if ch not in temp.children:
                temp.children[ch]=TrieNode()
            temp=temp.children[ch]
        temp.isEnd=True
    def search(self,word):
        root=self.root
        #print(root.isEnd)
        for ch in word:
            if not root:
                return False
            root = root.children[ch]
            # print(root.isEnd)
            # print(root.children.keys())
        if root.isEnd == True:
            return True
        else:
            return False
    # def findDiffrent(self,word):
    #     self.diff=0
    #     root=self.root
    #     lenth=len(word)
    #     for i in range(lenth):
    #         if not root and lenth-i>=1:
    #             return False
    #         print(root.children[word[i]])

A = ["data", "circle", "cricket"]
t=Trie()
for w in A:
    t.insert(w)
print(t.search("hello"))

