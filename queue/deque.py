class Node:
    def __init__(self,data):
        self.info=data
        self.next=None
        self.pre=None

class Deque:
    def __init__(self):
        self.font=None
        self.rear=None

    def is_empty(self):
        if self.font is None:
            return True

    def font_enqueue(self,x):
        temp=Node(x)
        if self.font is None:
            self.font=temp
            self.rear=temp
        else:
            temp.next=self.font
            self.font.pre=temp
            self.font=temp

    def font_dequeue(self):
        if self.font is None:
            print("font is empty")
        else:
            x=self.font.info
            self.font=self.font.next
            print(f"font dequeue element is {x}")

    def rear_enqueue(self,x):
        temp=Node(x)
        if self.rear is None:
            self.rear=temp
            self.font=temp
        else:
            temp.pre=self.rear
            self.rear.next=temp
            self.rear=temp

    def rear_dequeue(self):
        if self.rear is None:
            print("rear is empty")
        else:
            x=self.rear.info
            self.rear=self.rear.pre
            print(f"rear dequeue element is {x}")


    def display(self):
        p=self.font
        if self.font:
            print("deque is empty")
        else:
            while p is not None:
                print(p.info)
                p=p.next
queue=Deque()
while True:
    print("1 insert at front")
    print("2 insert at rear")
    print("3 delete at front")
    print("4 delete at rear")
    print("5 display list")
    print("7 quit")

    c=int(input("Enter the option"))
    if c==1:
        x=int(input("Enter the value"))
        queue.font_enqueue(x)
    if c==2:
        x=int(input("Enter the value"))
        queue.rear_enqueue(x)
    if c==3:
        queue.font_dequeue()
    if c==4:
        queue.rear_dequeue()
    if c==5:
        queue.display()
    if c==7:
        exit()
