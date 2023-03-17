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
        prev, this = None, self.root
        if self.root.data == data and this.left == None and this.right == None:
            self.root = None
            del this
            return data
        while this != None:
            if data > this.data:
                prev, this = this, this.right
            elif data < this.data:
                prev, this = this, this.left
            elif data == this.data:
                if this.left == None and this.right == None:
                    prev.left = (None if this.data < prev.data else prev.left)
                    prev.right = (None if this.data > prev.data else prev.right)
                elif this.left != None and this.right != None:
                    prev, this, pointer = this, this.left, this
                    if this.right == None:
                        prev.data, prev.left = this.data, this.left
                        if this.left != None:
                            prev.left = this.left
                        del this
                        return data
                    while this.right != None:
                        pointer, this = this, this.right
                    prev.data, pointer.right = this.data, this.right
                else:
                    if self.root.data == data:
                        self.root = (this.left if this.left != None else this.right)
                        del this
                        return data
                    prev.left = (this.left if this.left != None else this.right) if data < prev.data else prev.left
                    prev.right = (this.left if this.left != None else this.right) if data > prev.data else prev.right
                del this
                return data
        return None

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
            print("\nPreorder: ", end="")
            self.preorder(self.root)
            print("\nInorder: ", end="")
            self.inorder(self.root)
            print("\nPostorder: ", end="")
            self.postorder(self.root)

    def findMin(self, start):
        while start.left is not None:
            start = start.left
        return start.data

    def findMax(self, start):
        while start.right is not None:
            start = start.right
        return start.data

myBST = BST()
myBST.insert(14) 
myBST.insert(23) 
myBST.insert(7)
myBST.insert(10)
myBST.insert(33)
myBST.insert(5)
myBST.insert(20)
myBST.insert(13)
myBST.traverse()
print(" ")
myBST.delete(5)
myBST.traverse()
print(" ")
myBST.delete(33)
myBST.traverse()
print(" ")
myBST.delete(14)
myBST.traverse()
print(" ")
myBST.delete(7)
myBST.traverse()
print(" ")
myBST.delete(23)
myBST.traverse()
print(" ")
# print("\nMin:", myBST.findMin())
# print("Max:", myBST.findMax())