class SegmentTree:
    def __init__(self,lenth):
        self.lenth=lenth
        self.tree=[0 for i in range(4*self.lenth)]
    def buildTree(self,arr,low,high,pos):
        #print(low,high,pos)
        if low==high:
            self.tree[pos]=arr[low]
            return
        mid=low+(high-low)//2
        self.buildTree(arr,low,mid,2*pos+1)
        self.buildTree(arr,mid+1,high,2*pos+2)
        self.tree[pos]=self.tree[2*pos+1]+self.tree[2*pos+2]
    def quryTree(self,qury_strat,qury_end,pos,range_strat,range_end):
        if range_end<qury_strat or qury_end<range_strat:
            return 0
        elif range_strat>=qury_strat and range_end<=qury_end:
            return self.tree[pos]
        else:
            mid=range_strat+(range_end-range_strat)/2
            left=self.quryTree(qury_strat,qury_end,2*pos+1,range_strat,mid)
            right=self.quryTree(qury_strat,qury_end,2*pos+2,mid+1,range_end)
            return left+right
    



a=[1,3,5,7,9,11]
s=SegmentTree(len(a))
s.buildTree(a,0,len(a)-1,0)
print(s.quryTree(1,6,0,0,len(a)-1))


