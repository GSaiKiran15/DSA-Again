class MinStack:

    def __init__(self):
        self.minStack = []

    def push(self, val: int) -> None:
        self.minStack.append(val)
        return self.minStack

    def pop(self) -> None:
        self.minStack.pop(-1)
        return self.minStack

    def top(self) -> int:
        return self.minStack[-1]

    def getMin(self) -> int:
        return min(self.minStack)