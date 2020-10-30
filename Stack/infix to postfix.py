##implementation of stack using list
class Stack:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return self.items==[]

    def push(self,x):
        self.items.append(x)

    def pop(self):
        if self.is_empty():
            return -1
        else:
            x=self.items.pop()
            return x
    def display(self):
        print(self.items)

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]


def infix_to_postfix(infix):
    postfix=""
    stack=Stack()
    for symbol in infix:
        if symbol==' ' or symbol=="\t":
            continue
        if symbol =='(':
            stack.push(symbol)
        elif symbol==')':
            next=stack.pop()
            while next !=')':
                postfix=postfix+next
                next=stack.pop()
        elif symbol in '+-*/^':
            while not stack.is_empty() and precedence(stack.peek())>=precedence(symbol):
                postfix=postfix+stack.pop()

            stack.push(symbol)
        else:
            postfix+=symbol

    while not stack.is_empty():
        postfix=postfix+stack.pop()

    return postfix


def precedence(s):
    if s=='(':
        return 0
    if s=="+" or s=="-":
        return 1
    if s=="*" or s=="/" or s=="%":
        return 2
    if s=="^":
        return 3
    return 0

def postfix_eualuation(postfix):
    stack=Stack()
    for symbol in postfix:
        if symbol.isdigit():
            stack.push(int(symbol))
        else:
            x=stack.pop()
            y=stack.pop()
            if symbol=="+":
                stack.push(y+x)
            elif symbol=="-":
                stack.push(y-x)
            elif symbol=="*":
                stack.push(y*x)
            elif symbol=="/":
                stack.push(y/x)
            elif symbol=="%":
                stack.push(y%x)
            elif symbol=="^":
                stack.push(y^x)
    result=stack.pop()
    return result



for i in range(int(input())):
    infix=input("Enter infix expression")
    print(infix_to_postfix(infix))
    print(postfix_eualuation(infix_to_postfix(infix)))