class Stack:
    def __init__(self,max_size=10):
        self.item=[None]*max_size
        self.count=0
    def is_empty(self):
        if self.count==0:
            return True
    def is_full(self,max_size=10):
        if self.count==max_size:
            return True
    def push(self,x):
        if self.is_full():
            print("Stack is full")
        else:
            self.item[self.count]=x
            self.count+=1
    def pop(self):
        if self.is_empty():
            print("stack is empty")

        else:
            x=self.item[self.count-1]
            self.count-=1
            print(f"The pop value is {x}")
    def display(self):
        print(self.item)

stack=Stack()
while True:
    print("1 push ")
    print("2 pop")
    print("3 display")
    print("4 quit")
    c=int(input("Enter the option"))
    if c==1:
        x=int(input("Enter the value"))
        stack.push(x)
    if c==2:
        stack.pop()
    if c==3:
        stack.display()
    if c==4:
        exit()
