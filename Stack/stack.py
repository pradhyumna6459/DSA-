##implementation of stack using list
class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        if self.items==[]:
            return True
    def push(self,x):
        self.items.append(x)

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return
        else:
            x=self.items.pop()
            return x

    def size(self):
        return len(self.items)

    def display(self):
        print(self.items)


stack=Stack()
while True:
    print("1 push ")
    print("2 pop")
    print("3 is empty")
    print("4 size")
    print("5 diplay")
    print("6 quit")
    c=int(input("Enter the option"))
    if c==1:
        x=int(input("Enter the value"))
        stack.push(x)
    if c==2:
        x=stack.pop()
        print(f"pop element id {x}")
    if c==3:
        print(stack.is_empty())
    if c==4:
        print(f"the size of stack is {stack.size()}")
    if c==5:
        stack.display()
    if c==6:
        exit()
