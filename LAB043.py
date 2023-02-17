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

def infixToPostfix(expression, postfix=""):
    stack = ArrayStack()
    for i in expression:
        if i.isalpha():
            postfix += i
        elif i in "+-*/":
            if stack.is_empty():
                stack.push(i)
            else:
                if i in "+-":
                    while not stack.is_empty():
                        postfix += stack.pop()
                stack.push(i)
    while not stack.is_empty():
        postfix += stack.pop()
    return postfix

#def infixtopostfox(exp):
    stack = ArrayStack()
    operator = ['+', '-', '*', '/']
    priority = {'*':2, '/':2, '+':1, '-':1}
    ans = ''
    for i in exp:
        if i in operator:
            if stack.is_empty():
                stack.push(i)
            else:
                if priority.get(stack.stackTop()) > priority.get(i):
                    while not stack.is_empty():
                        x = stack.pop()
                        ans += str(x)
                    stack.push(i)
                else:
                    stack.push(i)
        else:
            ans += i
    while not stack.is_empty():
        x = stack.pop()
        ans += str(x)
    return ans
exp = "A+B*C-D/E"
postfix = infixToPostfix(exp)
print("Postfix of", exp, "is", postfix)
