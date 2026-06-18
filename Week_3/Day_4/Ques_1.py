class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print("After Push:", self.stack)

    def pop(self):
        if len(self.stack) == 0:
            print("Stack is Empty")
            return None

        item = self.stack.pop()
        print("Popped:", item)
        print("After Pop:", self.stack)
        return item

    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]


# Test
s = Stack()

s.push(1)
s.push(2)
s.push(3)
s.push(4)

print("Top Element:", s.peek())

s.pop()
s.pop()