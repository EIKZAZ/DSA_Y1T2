class DataNode:
    def __init__(self, name):
        self.name = name
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.count = 0
        self.head = None

    def traverse(self):
        if self.head == None:
            print("This is an empty list.")
        else:
            pos = self.head
            while pos != None:
                print(pos.name, end = "")
                pos = pos.next
                if pos != None:
                    print(" -> ", end = "")
                else:
                    print("")
        return

    def insertFront(self, data):
        pNew = DataNode(data)
        if self.head == None:
            self.head = pNew
        else:
            pNew.next = self.head
            self.head = pNew
        self.count += 1
        return

    def insertLast(self, data):
        pNew = DataNode(data)
        if self.head == None:
            self.head = pNew
        else:
            pos = self.head
            while pos.next != None:
                pos = pos.next
            pos.next = pNew
        return

    def insertBefore(self, node, data):
        pNew = DataNode(data)
        pos = self.head
        while pos.next != None:
            if pos.next.name == node:
                pNew.next = pos.next
                pos.next = pNew
                return
            pos = pos.next
        print("Cannont insert,"+ node + "does not exist.")

    def delete(self, data):
        pos = self.head
        if pos.name == data:
            self.head = self.head.next
            self.count -= 1
            return
        while pos.next != None:
            if pos.next.name == data:
                pos.next = pos.next.next
                self.count -= 1
                return
            pos = pos.next
        print("Cannot delete,", data, "dose not exist.")

        
mylist = SinglyLinkedList()
pNew = DataNode("John")
mylist.head = pNew
#print(mylist.head.name)
pNew = DataNode("Tony")
mylist.head.next = pNew
#print(mylist.head.next.name)
pNew = DataNode("Bill")
mylist.head.next.next = pNew
mylist.traverse()
mylist.insertFront("Kim")
mylist.traverse()
mylist.insertLast("EIK")
mylist.traverse()
mylist.insertBefore("EIK", "Rain")
mylist.traverse()
mylist.delete("Kim")
mylist.traverse()
