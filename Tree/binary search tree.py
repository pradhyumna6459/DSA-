class Node:
    def __init__(self,data):
        self.info=data
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def is_empty(self):
        return self.root==None

    def postorder(self):
        self.postorder1(self.root)
        print()

    def postorder1(self,p):
        if p is None:
            return
        self.postorder1(p.left)
        self.postorder1(p.right)
        print(p.info,end=" ")

    def inorder(self):
        self.inorder1(self.root)
        print()

    def inorder1(self,p):
        if p is None:
            return

        self.inorder1(p.left)
        print(p.info,end=" ")
        self.inorder1(p.right)

    def preorder(self):
        self.preorder1(self.root)
        print()


    def preorder1(self,p):
        if p is None:
            return
        print(p.info,end=" ")
        self.preorder1(p.left)
        self.preorder1(p.right)


    def search(self,x):
        return self.search1(x,self.root) is not None

    def search1(self,x,p):    #reccursive
        if p is None:
            return None
        if x<p.info:
            return self.search1(p.left,x)
        elif x>p.info:
            return self.search1(p.right,x)
        else:
            return p

    def search2(self,x): #non_recussive
        p=self.root
        while p is not None:
            if x<p.info:
                p=p.left
            elif x>p.info:
                p=p.right
            else:
                return True
        return False

    def small(self):
        p=self.root
        if self.is_empty():
            return
        if self.root is not None and  self.root.left is None:
            return self.root.info
        while p.left is not None:
            p=p.left
        return p.info

    def maximum_val(self):
        p=self.root
        if self.is_empty():
            return
        if self.root is not None and self.root.right is None:
            return self.root.info
        while p.right is not None:
            p=p.right
        return p.info

    def insertion(self,x):
        p=self.root
        par=None
        while p is not None:
            par=p
            if x<p.info:
                p=p.left
            elif x>p.info:
                p=p.right
            else:
                return
        temp=Node(x)
        if par ==None:
            self.root=temp
        elif x<par.info:
            par.left=temp
        else:
            par.right=temp

    def creation(self):
        n=int(input("Enter the number of node"))
        for i in range(n):
            x=int(input("Enter the value"))
            self.insertion(x)

    def display(self):
        self._display(self.root,0)
        print()


    def _display(self,p,level):
        if p is None:
            return
        self._display(p.right,level+1)
        print()
        for i in range(level):
            print("    ",end=" ")
        print(p.info)
        self._display(p.left,level+1)

    def delete(self,x):
        p=self.root
        par=None
        while p is not None:
            if p.info==x:
                break
            if p.info <x:
                p=p.left
            else:
                p=p.right
        if p is None:
            return

        if p.left !=None and p.right !=None:
            ps=p
            s=p.right
            while s.left is not None:
                ps=s
                s=s.left
            p.info=s.info
            p=s
            par=ps

        if p.left is not None:
            ch=p.left
        else:
            ch=p.right

        if par==None:
            self.root=ch
        elif p==par.left:
            par.left=ch
        else:
            par.right=ch
        




bt=BinarySearchTree()
bt.creation()
bt.display()
bt.inorder()


