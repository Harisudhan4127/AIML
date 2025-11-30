class Stack:
    def __init__(self):
        self.Stack = []
        
    def push(self, item):
        self.Stack.append(item)
        
    def pop(self):
        if not self.is_empty():
            return self.Stack.pop()
        raise IndexError("Pop From empty Stack")
    
    def peek(self):
        if not self.is_empty():
            return self.Stack[-1]
        raise IndexError("Peek From the Stack")
    
    def is_empty(self):
        return len(self.Stack) == 0
    
    def size(self):
        return len(self.Stack)
    
# Main code start
stack = Stack()
# Oject Created Stack
stack.push(1)
stack.push(2)
print("Peek : ", end="")
print(stack.peek())
print("Pop : ", end="")
print(stack.pop())
print("Empty Stack : ", end="")
print(stack.is_empty())
print("Stack Size : ", end="")
print(stack.size())