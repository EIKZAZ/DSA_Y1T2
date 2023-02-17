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

def is_parentheses_matching(expression):
    stack = ArrayStack()
    for i in expression:
        if i == "(":
            stack.push(i)
        elif i == ")":
            if not stack.is_empty():
                stack.pop()
            else:
                print("Parentheses in " + expression +" are unmatched")
                return False
    if stack.is_empty():
        return True
    else:
        print("Parentheses in " + expression +" are unmatched")
        return False

myStack = ArrayStack()
str = "((())))))((A-B*C))))))))))))))"
result = is_parentheses_matching(str)
print(result)