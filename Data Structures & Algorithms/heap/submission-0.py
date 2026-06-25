class MinHeap:
    
    def __init__(self):
        self.heap = [0]


    def siftUp(self, i: int) -> None:
        while i > 1 and self.heap[i] < self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i //= 2


    def siftDown(self, i: int) -> None:
        n = len(self.heap) - 1
        while 2 * i <= n:
            left = 2 * i
            right = left + 1

            # pick smaller child
            smallest = left
            if right <= n and self.heap[right] < self.heap[left]:
                smallest = right
            if self.heap[smallest] < self.heap[i]:
                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                i = smallest
            else:
                break

    def push(self, val: int) -> None:
        self.heap.append(val)

        i = len(self.heap) - 1
        #check if its greater than parent
        self.siftUp(i)

    def pop(self) -> int:
        if len(self.heap) <= 1:
            return -1

        if (len(self.heap) == 2):
            return self.heap.pop()

        res = self.heap[1]
        # move last to root, shrink, then sift down
        self.heap[1] = self.heap.pop()
        self.siftDown(1)

        return res

    def top(self) -> int:
        return self.heap[1] if len(self.heap) > 1 else -1

    def heapify(self, nums: List[int]) -> None:
        self.heap = [0] + nums

        for i in reversed(range(1, len(self.heap) // 2 + 1)):
            self.siftDown(i)
        