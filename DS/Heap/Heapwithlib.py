# import heapq
# class Heap:
#     def __init__(self,arr):
#         self.arr=arr
#     def genrate_min_heap(self):
#         heapq.heapify(self.arr)
#     def genrate_max_heap(self):
#         for index,elemn in enumerate(self.arr):
#             self.arr[index]=-elemn
#         heapq.heapify(self.arr)
#     def getmin(self):
#         heapq.heappop(self.arr)
#     def print_heap(self):
#         print(self.arr)
#
#
# arr=[2,3,4,5,6,1,7,8,1,1]
# h=Heap()
# h.genrate_heap(arr)
# h.print_heap()
#
