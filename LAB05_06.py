class BSTNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def is_empty(self):
        if self.root == None:
            return True
        else:
            return False

    def insert(self, data):
        pNew = BSTNode(data)
        if self.is_empty():
            self.root = pNew
        else:
            start = self.root
            while True:
                if data < start.data:
                    if start.left is None:
                        start.left = pNew
                        break
                    else:
                        start = start.left
                else:
                    if start.right is None:
                        start.right = pNew
                        break
                    else:
                        start = start.right

    def delete(self, data):
        if self.is_empty():
            print("This tree is emtpy!!!")
        else:
            start = self.root
            while True:
                if data < start.data:
                    if 

    def preorder(self, root):
        if (root != None):
            print("->", root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
        return

    def inorder(self, root):
        if (root != None):
            self.inorder(root.left)
            print("->", root.data, end=" ")
            self.inorder(root.right)
        return

    def postorder(self, root):
        if (root != None):
            self.postorder(root.left)
            self.postorder(root.right)
            print("->", root.data, end=" ")
        return

    def traverse(self):
        if self.is_empty():
            print("This tree is emtpy!!!")
        else:
            print("Preorder: ", end="")
            self.preorder(self.root)
            print("\nInorder: ", end="")
            self.inorder(self.root)
            print("\nPostorder: ", end="")
            self.postorder(self.root)

    def findMin(self):
        start = self.root
        while True:
            if start.left != None:
                start = start.left
            else:
                return start.data

    def findMax(self):
        start = self.root
        while True:
            if start.right != None:
                start = start.right
            else:
                return start.data

myBST = BST()
myBST.insert(14)
myBST.insert(23)
myBST.insert(7)
myBST.insert(10)
myBST.insert(33)
myBST.traverse()
myBST.delete(14)
myBST.traverse()
print("\nMin:", myBST.findMin())
print("Max:", myBST.findMax())
