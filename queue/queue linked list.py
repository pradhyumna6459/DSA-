class Node:
    def __init__(self,value):
        self.info=value
        self.link=None

class Queue:
    def __init__(self):
        self.font=None
        self.rear=None

    def is_empty(self):
        if self.font is None and self.rear is None:
            return True

    def enqueue(self,x):
        temp=Node(x)
        if self.is_empty():
            self.font=temp
            self.rear=temp
        else:
            p=self.font
            self.rear.link=temp
            self.rear=temp

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            x=self.font.info
            self.font=self.font.link
            print(f"dequeue element in list is {x}")


    def display(self):
        if self.is_empty():
            print("list is empty")
        else:
            p=self.font
            while p is not None:
                print(p.info)
                p=p.link

    def size(self):
        count=0
        p=self.font
        while p is not None:
            count=count+1
            p=p.link
        print(f"size of queue is {count}")
queue=Queue()
queue.dequeue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.display()
queue.dequeue()
queue.display()
queue.size()