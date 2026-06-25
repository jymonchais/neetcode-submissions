class DynamicArray:
    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.array = []

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if (len(self.array) < self.cap):
            self.array.append(n)
        else:
            self.resize()
            self.array.append(n)

    def popback(self) -> int:
        num = self.array[-1]
        self.array.pop(-1)

        return num

    def resize(self) -> None:
        self.cap *= 2

    def getSize(self) -> int:
        print()
        return len(self.array)
    
    def getCapacity(self) -> int:
        return self.cap
