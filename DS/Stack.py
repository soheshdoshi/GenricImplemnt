class Stack:
    def __init__(self,capacity):
        self.top=-1
        self.capacity=capacity
        self.array=[]
    def checkOverflow(self,capapcity):
        if self.capacity<capapcity:
            return 1
        return 0
    def checkUnderFlow(self,top):
        if top<-1:
            return 1
        return 0
    def push(self,value):
        if self.checkOverflow(self.top+1):
            return "StackOverFlow"
        self.array.append(value)
        self.top+=1
    def pop(self):
        if self.checkUnderFlow(self.top-1):
            return "StackUnderFlow"
        self.top-=1
        return self.array.pop()
    def peek(self):
        if self.top>-1:
            return self.array[0]
        return "StackEmpty"