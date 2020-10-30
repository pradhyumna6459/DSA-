class Queue:
    def __init__(self):
        self.item=[]
    def is_empty(self):
        if self.item ==[]:
            return True
    def enqueue(self,x):
        self.item.append(x)
    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty")
        else:
            x=self.item.pop(0)
            print(f"dequeue element is {x}")

    def size(self):
        return len(self.item)

    def display(self):
        if self.is_empty():
            print("list is empty")
        else:
            print(self.item)

'''queue=Queue()
queue.dequeue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.dequeue()
queue.display()'''
#optamize queue so that dequeue in o(1)
class Queue1:
    def __init__(self):
        self.item=[]
        self.front=0
    def is_empty(self):
        if self.front==len(self.item):
            return True
    def display(self):
        print(self.item)
    def size(self):
        return len(self.item)-self.front
    def enqueue(self,x):
        self.item.append(x)
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            x = self.item[self.front]
            self.item[self.front]=None
            self.front = self.front+1
            print(f"Dequeue element is{x}")

queue1=Queue1()
queue1.dequeue()
queue1.enqueue(1)
queue1.enqueue(2)
queue1.enqueue(3)
queue1.enqueue(4)
print(queue1.size())
queue1.dequeue()
queue1.display()



