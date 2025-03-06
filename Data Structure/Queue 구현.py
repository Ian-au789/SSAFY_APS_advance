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


# 원형 Queue를 구현해보자

class CircularQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity + 1           # front가 있는 칸은 사용 불가능하니 한 칸 더
        self.items = [None] * self.capacity
        self.front = 0                         # 원형으로 순환하니 배열 밖을 벗어나면 안됨
        self.rear = 0

    def enqueue(self, item):
        if self.is_full():
            raise IndexError("Queue is full")
        self.rear = (self.rear + 1) % self.capacity      # 배열 마지막 칸에 도달하면 자동으로 0번째 칸으로 돌아감
        self.items[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        self.front = (self.front + 1) % self.capacity    # 배열 마지막 칸에 도달하면 자동으로 0번째 칸으로 돌아감
        item = self.items[self.front]
        self.items[self.front] = None
        return item

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[(self.front + 1) % self.capacity]

    def get_size(self):
        return (self.rear - self.front + self.capacity) % self.capacity   # front에서 rear까지 칸의 개수, front가 rear보다 뒤에 있을 경우 고려
