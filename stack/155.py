#155 最小栈
class MinStack :
    def __init__(self) :
        self.stack = []
        self.minimum = {}
    def push(self,val) :
        self.stack.append(val)
        index = len(self.stack)-1
        if index == 0 :
            self.minimum[index] = val
        else:
            self.minimum[index] = min(val,self.minimum[index - 1])
    def pop(self) :
        index = len(self.stack) - 1
        self.stack.pop()
        del self.minimum[index]
    def top(self) :
        return self.stack[-1]
    def getMin(self) :
        index = len(self.stack) - 1
        return self.minimum[index]

#依旧键值对这一块