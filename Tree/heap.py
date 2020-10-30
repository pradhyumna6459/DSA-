import math
class Heap:
    def __init__(self,max_size=10):
        self.a=[None]*max_size
        self.n=0
        self.a[0]=99999
    def display(self):
        print(self.a)

    def insert(self,x):
        self.n+=1
        self.a[self.n]=x
        self.restore(self.n)

    def restore(self,i):
        k=self.a[i]
        parent=math.floor(i/2)
        while self.a[parent]<k:
            self.a[i]=self.a[parent]
            i=parent
            parent=math.floor(i/2)
        self.a[i]=k

    def creation(self):
        n=int(input("Number of node "))
        for i in range(n):
            x=int(input("Enter the value"))
            self.insert(x)
    def deletion(self):
        max_value=self.a[1]
        self.a[1]=self.a[self.n]
        self.n-=1
        self.restoreup(self.n)
        return max_value

    def restoreup(self,i):
        k=self.a[i]
        left=2*i
        right=2*i+1
        while right<=self.n:
            if k>=self.a[left] and k>=self.a[right]:
                self.a[i]=k
                return
            else:
                if self.a[left]>self.a[right]:
                    self.a[i]=self.a[left]
                    i=left
                else:
                    self.a[i]=self.a[right]
                    i=right
            left=2*i
            right=left+1
        if left==self.n and k<self.a[left]:
            self.a[i]=self.a[left]
            i=left
        self.a[i]=k

heap=Heap()
heap.creation()
heap.display()