class ArrayStack:
    def __init__(self):
        self.data = []
    
    def size(self):
        return len(self.data)

    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    def push(self, input_data):
        self.data.append(input_data)
        return self.data

    def pop(self):
        if self.is_empty():
            print("Underflow: Cannot pop data from an empty list")
            return None
        else:
            return self.data.pop()

    def stackTop(self):
        if self.is_empty():
            return None
        else:
            self.data[-1]

    def printStack(self):
        print(self.data)

def copyStack(stack1, stack2):
    stack_check = ArrayStack()
    while stack2.data != []:
        stack2.pop()
    while stack1.data != []:
        x = stack1.pop()
        stack_check.push(x)
    while stack_check.data != []:
        x = stack_check.pop()
        stack1.push(x)
        stack2.push(x)

s1 = ArrayStack()
s1.push(10); s1.push(20); s1.push(30)
s2 = ArrayStack()
s2.push(15)
copyStack(s1, s2)
s1.printStack()
s2.printStack()