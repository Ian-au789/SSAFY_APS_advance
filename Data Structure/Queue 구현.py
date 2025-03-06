# Class로 Queue를 구현해보자

class Queue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        if self.is_full():
            raise IndexError("Queue is full")
        self.rear += 1
        self.items[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        self.front += 1
        item = self.items[self.front]
        self.items[self.front] = None
        return item

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return self.rear == self.capacity - 1

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[self.front + 1]

    def get_size(self):
        return self.rear - self.front


queue1 = Queue(15)

queue1.enqueue(1)
queue1.enqueue(5)
queue1.enqueue(9)

q1 = queue1.dequeue()
q2 = queue1.dequeue()

print(q1)
print(q2)
