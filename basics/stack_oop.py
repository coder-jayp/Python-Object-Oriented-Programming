class Stack:
    def __init__(self, max_size=5):
        self.stack = []
        self.max_size = max_size

    def push(self, x):
        if len(self.stack) >= self.max_size:
            raise OverflowError("❌ Stack Overflow: Cannot push, stack is full!")
        self.stack.append(x)
        print(f"Pushed {x} -> Stack: {self.stack}")

    def pop(self):
        if self.is_empty():
            raise IndexError("❌ Stack Underflow: Cannot pop, stack is empty!")
        popped = self.stack.pop()
        print(f"Popped {popped} -> Stack: {self.stack}")
        return popped

    def peek(self):
        if self.is_empty():
            raise IndexError("❌ Cannot peek, stack is empty!")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


stack = Stack(max_size=5)

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

try:
    stack.push(60)
except OverflowError as e:
    print(e)

print("Top element is:", stack.peek())

stack.pop()
stack.pop()

print("Current stack size:", stack.size())

stack.pop()
stack.pop()
stack.pop()

try:
    stack.pop()
except IndexError as e:
    print(e)