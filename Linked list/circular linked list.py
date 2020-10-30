class Node:
    def __init__(self,value):
        self.info=value
        self.link=None

class circular:
    def __init__(self):
        self.last=None
    def display(self):
        if self.last is None:
            print("list is empty")
        else:
            p=self.last.link
            while True:
                print(p.info)
                p=p.link
                if p==self.last.link:
                    break

    def insert_at_beg(self,x):
        temp=Node(x)
        temp.link=self.last.link
        self.last.link=temp

    def insert_at_empty_list(self,data):
        temp=Node(data)
        self.last=temp
        self.last.link=self.last

    def insert_at_end(self,data):
        temp=Node(data)
        temp.link=self.last.link
        self.last.link=temp
        self.last=temp

    def insert_after(self,x,data):
        p=self.last.link
        while True:
            if p.info==x:
                break
            p=p.link
            if p==self.last.link:
                break
        if p==self.last.link and p.info !=x:
            print("x is not found")
        else:
            temp=Node(data)
            temp.link=p.link
            p.link=temp
            if p==self.last:
                self.last=temp

    def creation(self):
        n=int(input("Enter the value of n"))
        if n==0:
            return
        x=int(input("Enter the value"))
        self.insert_at_empty_list(x)
        for i in range(n-1):
            x=int(input("Enter the value"))
            self.insert_at_end(x)

    def del_at_beg(self):
        if self.last is None:
            print("list is empty")
        elif self.last==self.last.link:
            self.last=None
        else:
            self.last.link=self.last.link.link

    def del_at_end(self):
        p=self.last.link
        while p.link is not self.last:
            p=p.link
        p.link=self.last.link
        self.last=p

    def del_at_pos(self,x):
        if self.last is None:
            print("List is empty")
        if self.last==self.last.link and self.last.info==x:
            self.last=None

        if self.last.link.info==x:
            self.last.link=self.last.link.link
            return
        p=self.last.link
        while p.link !=self.last.link:
            if p.link.info==x:
                break
            p=p.link
        if p.link==self.last.link:
            print("X is not fount")
        else:
            p.link=p.link.link
            if self.last.info==x:
                self.last=p


    def con(self,list1):
        if self.last is None:
            self.last=list1
            return
        if list1.last is None:
            return
        p=self.last.link
        self.last.link=list1.last.link
        list1.last.link=p
        self.last=list1.last








list=circular()
list.creation()
list1=circular()
list1.creation()
#list.display()
#list.insert_at_beg(6)
#list.display()
#list.insert_at_end(7)
#list.display()
#list.insert_after(4,5)
#list.display()
#list.del_at_end()
#list.del_at_beg()
#list.display()
#list.del_at_end()
#list.display()
#list.del_at_pos(4)
#list.display()
list.con(list1)
list.display()