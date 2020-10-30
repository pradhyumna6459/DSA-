class Node:
    def __init__(self,x):
        self.info=x
        self.link=None

class Queue:
    def __init__(self):
        self.rear=None
    def is_empty(self):
        if self.rear is None:
            return True
    def enqueue(self,x):
        temp=Node(x)
        if self.is_empty():
            self.rear=temp
            self.rear.link=temp
        else:
            temp.link=self.rear.link
            self.rear.link=temp
            self.rear=temp

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        elif self.rear.link==self.rear:
            x=self.rear.info
            self.rear=None
            print(f"dequeue element is {x}")

        else:
            temp=self.rear.link
            x=temp.info
            self.rear.link=temp.link
            print(f"dequeue element is {x}")

    def size(self):
        p=self.rear.link

        count=0
        while p !=self.rear.link:
            count=count+1
            p=p.link
        print(f"Number of element in list {count}")

    def display(self):
        if self.is_empty():
            print("list is empty")
        else:
            p=self.rear.link
            while True:
                print(p.info)
                p=p.link
                if p==self.rear.link:
                    break1

queue=Queue()
#queue.dequeue()
#queue.display()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.dequeue()
queue.display()