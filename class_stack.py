class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if not self.stack:
            return True
        return False

    def push(self, add):
        self.stack.append(add)

    def pop(self):
        if self.is_empty():
            return None
        result = self.stack.pop()
        return result

    def peek(self):
        if self.is_empty():
            return None
        peek = self.stack[-1]
        return peek
    def size(self):
        return len(self.stack)



