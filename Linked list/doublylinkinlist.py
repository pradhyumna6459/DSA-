class Node:
    def __init__(self,value):
        self.info=value
        self.pre=None
        self.next=None
class doublelinkinlist:
    def __init__(self):
        self.start=None

    def display(self):
        if self.start==None:
            print("List is empty")
        temp=self.start
        while temp is not None:
            print(temp.info)
            temp=temp.next

    def insert_at_beg(self,data):
        temp=Node(data)
        if self.start is None:
            self.start=temp
        else:
            temp.next=self.start
            self.start.pre=temp
            self.start=temp

    def insert_at_last(self,data):
        temp=Node(data)
        if self.start is None:
            self.start=temp
        p=self.start
        while p.next is  not None:
            p=p.next

        temp.pre=p
        p.next=temp

    def insertion_after_node(self,x,data):
        if self.start is None:
            return
        temp=Node(data)
        p=self.start
        while p is not None:
            if p.info ==x:
                break
            p=p.next
        #print(p.info)
        if p is None:
            print(f'{x} is not found')
        else:
            temp.pre = p
            temp.next = p.next
            if p.next is not None:
                p.next.pre = temp
                p.next = temp

    def insertion_before_node(self,x,data):
        temp=Node(data)
        p=self.start
        while p is not None:
            if p.info==x:
                break
            p=p.next
        if p is None:
            print("Insertion is not possible")
        else:
            temp.next=p
            temp.pre=p.pre
            p.pre.next=temp
            p.pre=temp

    def creation(self):
        n=int(input("Enter the value of n"))
        if n==0:
            return
        data=int(input("Enter value"))
        self.insert_at_beg(data)

        for i in range(n-1):
            data=int(input("Enter value"))
            self.insert_at_last(data)

    def del_beg(self):
        if self.start is None:
            print("Not possible")
        if self.start.next is None:
            self.start=None
            return
        else:
            self.start=self.start.next
            self.start.pre=None

    def del_end(self):
        if self.start is None:
            print("Not possible")
            return
        if self.start.next is None:
            self.start=None
            return
        else:
            p=self.start
            while p.next is not None:
                p=p.next
            p.pre.next=None

    def del_at_given_node(self,x):
        if self.start is None:
            print("Not possible")
            return
        if self.start.next is None:
            if self.start.info==x:
                self.start=None
            else:
                print(" x not found")
        if self.start.info==x:
            self.start = self.start.next
            self.start.pre = None

        p=self.start
        while p.next is not None:
            if p.info==x:
                break
            p=p.next
        if p.next is not None:
            p.pre.next = p.next
            p.next.pre = p.pre
        else:
            p.pre.next=None
    def reverse(self):
        p1=self.start
        p2=p1.next
        p1.next=None
        p1.pre=p2
        while p2 is not None:
            p2.pre=p2.next
            p2.next=p1
            p1=p2
            p2=p2.pre
        self.start=p1












list=doublelinkinlist()
list.creation()
#list.display()
#list.insert_at_beg(50)
#list.display()
#list.insert_at_last(45)
#list.display()
#list.insertion_after_node(5,12)
#list.display()
#list.insertion_before_node(4,10)
#list.display()
#list.del_beg()
#list.display()
#list.del_end()
#list.display()
#list.del_at_given_node(4)
#list.display()
list.reverse()
list.display()