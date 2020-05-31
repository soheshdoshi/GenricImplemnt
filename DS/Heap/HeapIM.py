"""
1) build heap
2) insert
3) delete
4) min/max
5)top_down
6)down-top
"""

class Heap:
    def __init__(self):
        self.heapList=[0]
        self.currentSize=0
    def down_top(self,index):
        while index//2>0:
            curr_elem=self.heapList[index]
            parent_elem=self.heapList[index//2]
            if curr_elem<parent_elem:
                curr_elem,parent_elem=parent_elem,curr_elem
            index=index//2
    def insert(self,valeu):
        self.heapList.append(valeu)
        self.currentSize+=1
        self.down_top(self.currentSize)

