# class로 stack을 구현해보자

class Stack:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.items = [None] * capacity
        self.top = -1

    def push(self, item):
        if self.is_full():
            raise IndexError("Stack is full")

        self.top += 1
        self.items[self.top] = item

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")

        item = self.items[self.top]
        self.items[self.top] = None
        self.top -= 1
        return item

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def peek(self):
        if self.is_empty():
            IndexError("Stack is empty")

        return self.items[self.top]

    def get_size(self):
        return self.top + 1


stack1 = Stack(15)

stack1.push(1)
stack1.push(5)
stack1.push(9)

s1 = stack1.pop()
s2 = stack1.pop()

print(s1)
print(s2)
