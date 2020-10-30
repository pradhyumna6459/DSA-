class Node:
    def __init__(self,value):
        self.info=value
        self.link=None

class Singlelinkedlist:
    def __init__(self):
        self.start=None

    def order_insertion(self,x):
        temp=Node(x)
        if self.start is None or x <self.start.info:
            temp.link=self.start
            self.start=temp
            return

        p = self.start
        while p.link is not None and p.link.info<=x:
            p = p.link
        temp.link = p.link
        p.link = temp
            #print(temp.info,p.
    def display(self):
        if self.start is None:
            print("list is empty")
        else:
            p=self.start
            while p:
                print(p.info)
                p=p.link

    def creation(self):
        n=int(input("Enter the value of node"))
        if n==0:
            return
        for i in range(n):
            x = int(input("Enter the value"))
            self.order_insertion(x)



list=Singlelinkedlist()
list.creation()
list.display()
