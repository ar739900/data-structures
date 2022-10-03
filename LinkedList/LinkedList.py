class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"Node({self.data})"

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __repr__(self):
        repr = ""
        current = self.head
        while current:
            repr += str(current.data)
            repr += "->"
            current = current.next
        repr += "None"
        return repr

    def __len__(self):
        return self.size

    def addLast(self,item):
        node = Node(item)
        if self.size == 0:
            self.head = self.tail =  node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def isEmpty(self):
        return self.size == 0

    def addFirst(self,item):
        node = Node(item)
        if self.size == 0:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def insert(self, position, item):
        previous = None
        current = self.head

        for i in range(position):
            previous = current
            current = current.next

        node = Node(item)
        previous.next = node
        node.next = current

    def indexOf(self,item):
        index = 0
        current = self.head
        while current:
            index += 1
            if current.data == item:
                return index
            current = current.next
        return -1

    def removeFirst(self):
        if self.head == self.tail:
            return
        if self.size == 1:
            self.head = self.tail = None
            return
        second = self.head.next
        self.head = None
        self.head = second

        self.size -= 1

    def removeLast(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = self.tail = None
            self.size-=1
            return
        current = self.head
        while current.next != self.tail and current.next.next != None:
            current = current.next
        current.next = None
        self.tail = current

        self.size-=1
