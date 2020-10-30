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

def check_expression(expression):
    stack=Stack()

    for ch in expression:
        if ch in '([{':
            stack.push(ch)
        if ch in ')]}':
            if stack.is_empty():
                return False
            else:
                char=stack.pop()
                if not is_equal(ch,char):
                    return False




    if stack.is_empty():
        return True
    else:
        return False



def is_equal(ch,char):
    if ch ==']' and char =='[':
        return True
    if ch =='}' and char =='{':
        return True
    if ch ==')' and char =='(':
        return True
    return  False

for i in range(int(input())):
    s=input("Enter expression")
    if check_expression(s):
        print("valid")
    else:
        print("invalid")