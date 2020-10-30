from collections import  deque
class Node:
    def __init__(self,data):
        self.info=data
        self.lchild=None
        self.rchild=None
s=[]
class BinaryTree:
    def __init__(self):
        self.root=None

    def is_empty(self):
        return self.root==None

    def create(self):
        self.root = Node('p')
        self.root.lchild = Node('q')
        self.root.rchild = Node('r')
        self.root.lchild.lchild = Node('a')
        self.root.lchild.rchild = Node('b')
        self.root.rchild.rchild = Node('x')

    def display(self):
        self._display(self.root,0)
        print()


    def _display(self,p,level):
        if p is None:
            return
        self._display(p.rchild,level+1)
        print()
        for i in range(level):
            print("    ",end=" ")
        print(p.info)
        self._display(p.lchild,level+1)

    def preorder(self):
        self.preorder1(self.root)
        print()

    def preorder1(self,p):
        if p is None:
            return
        print(p.info,end=" ")
        self.preorder1(p.lchild)
        self.preorder1(p.rchild)

    def inorder(self):
        self.inorder1(self.root)
        print()
    def inorder1(self,p):
        if p is None:
            return
        self.inorder1(p.lchild)
        print(p.info,end=" ")
        s.append(p.info)
        self.inorder1(p.rchild)

    def postorder(self):
        self.postorder1(self.root)
        print()

    def postorder1(self,p):
        if p is None:
            return
        self.postorder1(p.lchild)
        self.postorder1(p.rchild)
        print(p.info,end=" ")

    def level_order(self):
        qu=deque()
        if self.root is None:
            return
        s=""
        qu.append(self.root)
        while len(qu)!=0:
            p=qu.popleft()
            s=s+str(p.info)+" "
            if p.lchild is not None:
                qu.append(p.lchild)
            if p.rchild is not None:
                qu.append(p.rchild)

        return s

    def height_of_binarytree(self):
        return self.height1(self.root)
    def height1(self,p):
        if p is None:
            return 0
        hl=self.height1(p.lchild)
        hr=self.height1(p.rchild)
        s=1+max(hr,hl)
        return s



bt=BinaryTree()
bt.create()
bt.display()
#bt.preorder()
bt.inorder()
print(s)
#bt.postorder()
#print(bt.level_order())
#print(bt.height_of_binarytree())