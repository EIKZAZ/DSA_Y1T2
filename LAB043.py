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
            return self.data[-1]

    def printStack(self):
        print(self.data)

def infixToPostfix(expression):
    stack = ArrayStack()
    postfix = ""
    for i in expression:
        if i.isalpha():
            postfix += i
        else:
            if not stack.is_empty():
                if (i in ["+", "-"]) and (stack.stackTop() in ["*", "/", "+", "-"]):
                    for _ in range(stack.size()):
                        postfix += stack.pop()
                if (i in ["*", "/"]) and (stack.stackTop() in ["*", "/"]):
                    postfix += stack.pop()
            stack.push(i)
    if not stack.is_empty():
        for _ in range(stack.size()):
            postfix += stack.pop()
    return postfix

exp = "A+B*C/D-E+F*G"
postfix = infixToPostfix(exp)
print("Postfix of", exp, "is", postfix)
