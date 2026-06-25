class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        new = Node(value)
        lastNode = self.tail.prev

        lastNode.next = new
        new.next = self.tail
        self.tail.prev = new
        new.prev = lastNode

    def appendleft(self, value: int) -> None:
        new = Node(value)
        firstNode = self.head.next

        firstNode.prev = new
        new.prev = self.head
        new.next = firstNode
        self.head.next = new

        
    def pop(self) -> int:
        if self.isEmpty():
            return -1

        lastN = self.tail.prev
        val = lastN.value

        prevN = lastN.prev
        prevN.next = self.tail
        self.tail.prev = prevN

        return val


    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        firstN = self.head.next
        value = firstN.value
        nextN = firstN.next

        self.head.next = nextN
        nextN.prev = self.head

        return value
