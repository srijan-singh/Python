# Stack is a user defined function
# It follows LIFO (Last In First Out) principle
class Stack():
    def __init__(self):
        self.stack = list()
    # Push function is used to add items at last position in Stack
    def push(self, item):
        self.stack.append(item)
    # Pop function is used to remove the last item in Stack
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None
    # Peek function is used to view the last item
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        else:
            return None
    def __str__(self):
        return str(self.stack)

my_stack = Stack()

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print(my_stack.pop())
print(my_stack.pop())


