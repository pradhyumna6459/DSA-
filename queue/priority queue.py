class Node:
    def __init__(self,pre,value):
        self.pre=pre
        self.info=value
        self.next=None

class PriorityQueue:
    def __init__(self):
        self.front=None
    def is_empty(self):
        return self.front==None

    def enqueue(self,pre,data):
        temp=Node(pre,data)
        if self.is_empty() or self.front.pre>pre:
            self.front=temp
        else:
            p=self.front
            while p.next !=None and p.next.pre<=pre:
                p=p.next
            temp.next=p.next
            p.next=temp

    def dequeue(self):
        if self.is_empty():
            print("priority queue is empty")
        else:
            x=self.front.info
            x1=self.front.pre
            self.front=self.front.next

            print(f"Dequeue element is {x} and priority is {x1}")

    def display(self):
        if self.is_empty():
            print("list is empty")
        else:
            p=self.front
            while p is not None:
                print(p.info)
                p=p.next

queue=PriorityQueue()
while True:
    print("1 enqueue")
    print("2 dequeue")
    print("3 display")
    print("4 quit")

    c=int(input("Enter the option"))
    if c==1:
        x=int(input("Enter the value"))
        x1=int(input("Enter the priority"))
        queue.enqueue(x1,x)
    if c==2:
        queue.dequeue()
    if c==3:
        queue.display()
    if c==4:
        exit()