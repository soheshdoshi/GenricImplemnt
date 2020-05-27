# class MinHeap:
#     def __init__(self):
#         self.heapList=[0]
#         self.currentsize=0
#     def down_top(self,index):
#         while index//2>0:
#             if self.heapList[index]<self.heapList[index//2]:
#                 self.heapList[index],self.heapList[index//2]=self.heapList[index//2],self.heapList[index]
#             index=index//2
#
#     def top_down(self,index):
#         while 2*index<=self.currentsize:
#
#
#
