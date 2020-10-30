class Node:
    def __init__(self,data):
        self.info=data
        self.link=None
class Stack:
    def __init__(self):
        self.top=None

    def is_empty(self):
        if self.top is None:
            return True

    def push(self,x):
        temp=Node(x)
        if self.is_empty():
            self.top=temp
        else:
            temp.link=self.top
            self.top=temp
    def pop(self):
        if self.is_empty():
            print("Stack is under flow")
        else:
            x=self.top.info
            self.top=self.top.link
            print(f"The poped element is {x}")
    def display(self):
        if self.is_empty():
            print("list is empty")
        else:
            p=self.top
            while p is not None:
                print(p.info)
                p=p.link


stack=Stack()
stack.pop()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.pop()
stack.pop()
stack.display()