'''
author:"Pradhyumna SIngh Rathore"
'''

#linkin list
class Node:
    def __init__(self,data):
        self.info=data
        self.link=None

class SingleLinkedlist:
    def __init__(self):
        self.start=None

    def display(self):
        if self.start==None:
            print("List is empty")
        else:
            temp=self.start
            while(temp):
                print(temp.info)
                temp=temp.link

    def count(self):
        temp=self.start
        count=0
        while(temp):
            count=count+1
            temp=temp.link
        return count

    def search(self,x):
        temp=self.start
        flag=False
        while(temp):
            if temp.info==x:
                flag=True
                break
            temp=temp.link

        if flag==True:
            print("The Element is present")
        else:
            print("Tu ja rey")

    def insert_beg(self,data):
        temp=Node(data)
        if self.start==None:
            self.start=temp

        else:
            temp.link=self.start
            self.start=temp
    def insert_end(self,data):
        p=Node(data)
        temp=self.start
        if self.start==None:
            self.start=p
        else:
            while temp.link is not None:
                temp=temp.link

            temp.link=p

    def create(self):
        print("insert number of node")
        n=int(input())
        for i in range(n):
            x=int(input())
            self.insert_end(x)

    def after_node(self,x,data):
        p=Node(data)
        temp=self.start
        while temp is not None:
            if temp.info==x:
                break
            temp=temp.link

        if temp is None:
            print("Element x is not present")
        else:
            p.link = temp.link
            temp.link = p


    def node_before(self,x,data):
        p=Node(data)
        temp=self.start
        if self.start.info==x:
            p.link=self.start
            self.start=p

        else:
            while temp.link is not None:
                if temp.link.info==x:
                    break
                temp=temp.link


            if temp.link is None:
                temp.link=p

            else:
                p.link=temp.link
                temp.link=p

    def insert_at_pos(self,k,data):
        p=Node(data)
        temp=self.start
        i=1
        while( i<k-1 and temp is not None):
            temp=temp.link
            i+=1
        if temp is None:
            print("Insertion not possible")
        else:
            p.link = temp.link
            temp.link = p

    def delete(self,x):
        if self.start is None:
            print("list is empty")

        if self.start.info==x:
            self.start=self.start.link

        else:
            temp=self.start
            while temp.link is not None:
                if temp.link.info==x:
                    break
                temp=temp.link

            temp.link=temp.link.link
    def del_first(self):
        if self.start is None:
            print("list is empty")

        self.start=self.start.link

    def last_del(self):
        if self.start is None:
            print("list is empty")
        else:
            temp=self.start
            while temp.link.link is not None:
                temp=temp.link

            temp.link=None

    def reverse_list(self):
        pre=None
        p=self.start
        while p is not None:
            next=p.link
            p.link=pre
            pre=p
            p=next

        self.start=pre

    def sort_bubble_data(self):
        end=None

        while end !=self.start.link:
            p = self.start
            while p.link !=end:
                q=p.link
                if p.info > q.info:
                    p.info,q.info=q.info,p.info
                p=p.link
            end=p

    def merge(self,list2):
        merge_list=SingleLinkedlist()
        merge_list.start=self.merge1(self.start,list2.start)
        return merge_list

    def merge1(self,p1,p2):
        if p1.info<=p2.info:
            startM=Node(p1.info)
            p1=p1.info
        else:
            startM=Node(p2.info)
            p2=p2.info
        pm=startM
        while p1 is not None and p2 is not None:
            if p1.info <= p2.info:
                pm.link = Node(p1.info)
                p1 = p1.info
            else:
                pm.link= Node(p2.info)
                p2 = p2.info
        pm = pm.link

        while p1 is not None:
            pm.link=Node(p1.info)
            p1=p1.link
            pm=pm.link
        while p2 is not None:
            pm.link=Node(p2.info)
            p2=p2.link
            pm=pm.link

        return startM

    def find_cycle(self):
        if self.has_cycle() is None:
            return False
        else:
            return True

    def has_cycle(self):
        p=self.start
        q=self.start
        if self.start is None or self.start.link is None:
            return None
        else:
            while q is not None and q.link is not None:
                p=p.link
                q=q.link.link
                if p==q:
                    return p
            return None


    def insert_cycle(self,x):
        p=self.start
        pre=self.start
        px=None
        while p.link is not None:
            if p.link.info==x:
                px=p
            p=p.link
        p.link=px

    def find_middle(self):
        temp,temp1=self.start,self.start
        while temp is not None and temp.link is not None:
            temp=temp.link.link
            temp1=temp1.link
        print(temp1.info)













list=SingleLinkedlist()
#creation  of list
list.create()
#insert at end
#list.insert_end(8)
#display
#list.display()
#insertion after given node
#display list
#list.display()

#deletion of node
#list.delete(45)
#list.display()
#list.del_first()
#list.display()
#list.last_del()
#list.display()
#list.reverse_list()
#list.display()
#list.sort_bubble_data()
#ist.display()
#list.insert_cycle(40)
#print(list.find_cycle())
list.find_middle()