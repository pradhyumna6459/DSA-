class Deque:
    def __init__(self):
        self.item=[]
    def is_empty(self):
        if self.item==[]:
            return True
    def display(self):
        if self.is_empty():
            print("list is empty")
        else:
            print(self.item)
    def font_enqueue(self,x):
        self.item.insert(0,x)
    def rear_enqueue(self,x):
        self.item.append(x)
    def rear_dequeue(self):
        if self.is_empty():
            print("deque is empty")
        else:
            x=self.item.pop()
            print(f"dequeue element is {x}")
    def font_dequeue(self):
        if self.is_empty():
            print("Deque is empty")
        else:
            x=self.item.pop(0)
            print(f"dequeue element is {x}")

    def size(self):
        return len(self.item)


queue=Deque()
while True:
    print("1 insert at front")
    print("2 insert at rear")
    print("3 delete at front")
    print("4 delete at rear")
    print("5 display list")
    print("6 size of list")
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
    if c==6:
        print(f"size of queue is {queue.size()}")
    if c==7:
        exit()


