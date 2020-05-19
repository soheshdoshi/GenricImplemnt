from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children=defaultdict(TrieNode)
        self.isEnd=False

class Solution:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        root=self.root
        for ch in word:
            if ch not in root.children:
                root.children[ch]=TrieNode()
            root=root.children[ch]
        root.isEnd=True

    def find_charter_node(self,ch,index):



A = ["hello", "world"]
B = ["hella", "pello", "pella"]
s=Solution()
for i in A:
    s.insert(i)
s.checkFunction("p")
