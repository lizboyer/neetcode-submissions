class MinStack:

    def __init__(self):
        self.minStack = []
        self.min_item = []
        self.min_item.append(2**31)
    def push(self, val: int) -> None:
        # print("push:", self.minStack)
        # print("get min:", self.min_item)

        self.minStack.append(val)
        # print("# print:",self.min_item[0])
        if val <= self.min_item[-1]:
            self.min_item.append(val)
        # print("get min after:", self.min_item)

        # print("push after:", self.minStack)

    def pop(self) -> None:
        # print("pop:", self.minStack)
        # print(" pop mins:", self.min_item)

        if self.min_item[-1] == self.minStack[-1]: self.min_item.pop(-1)
        self.minStack.pop(-1)
        # print("after pop mins:", self.min_item)

        # print("after pop:", self.minStack)

    def top(self) -> int:
        # print("top:", self.minStack)
        return(self.minStack[-1])

    def getMin(self) -> int:
        # print("  GET MIN:", self.minStack)
        # print("  MINS:", self.min_item)

        tmp = self.min_item.copy()
        tmp.sort()
        # print("get min after:", self.minStack)

        return(tmp[0])
        # min_item = 2^31 - 1
        # for i in range(len(self.minStack)):
        #     min_item = min(min_item, self.minStack[i])
        # return(min_item)
