from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.frq = 0
        self.isEnd = False


class Solution:
    # @param A : list of strings
    # @return a list of strings
    def __init__(self):
        self.root = TrieNode()
        self.ans = []

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch].frq += 1
                node.children[ch] = TrieNode()
                # node.frq+=1
            node.children[ch].frq += 1
            node = node.children[ch]
            # node.frq+=1
        node.isEnd = True

    def checkFrq(self, word):
        node = self.root
        s = ""
        for ch in word:
            if node.children[ch].frq < 2:
                s += ch
                self.ans.append(s)
                break
            else:
                s += ch
                node = node.children[ch]

    def print_ans(self):
        return self.ans

        def prefix(self, A):
            for word in A:
                self.insert(word)
            for word in A:
                self.checkFrq(word)
            return self.print_ans()



