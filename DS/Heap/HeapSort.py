import heapq


arr=[2,3,1,4,5,6,11,23,45]

temp=[]
heapq.heapify(arr)
for i in range(len(arr)):
    temp.append(heapq.heappop(arr))
print(temp)