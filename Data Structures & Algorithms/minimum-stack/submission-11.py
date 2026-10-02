class MinStack:
    def __init__(self):
        self.minStack = []
        self.min_item = []
        self.min_item.append(2**31)
    def push(self, val: int) -> None:
        self.minStack.append(val)
        if val <= self.min_item[-1]:
            self.min_item.append(val)

    def pop(self) -> None:
        if self.min_item[-1] == self.minStack[-1]: self.min_item.pop(-1)
        self.minStack.pop(-1)

    def top(self) -> int:
        return(self.minStack[-1])

    def getMin(self) -> int:
        tmp = self.min_item.copy()
        tmp.sort()
        return(tmp[0])

