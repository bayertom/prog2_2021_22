class Node:
    def __init__(self, data):
        self.data = data
        self.next : Node =  None

    def print(self):
        print(self.data)

class Node2:
    def __init__(self, data):
        self.data = data
        self.prev: Node = None
        self.next : Node =  None

    def print(self):
        print(self.data)


class LList:
    def __init__(self):
        self.first : Node = None
        self.last: Node = None

    def push (self, data):
        #Create new node
        n = Node(data)

        #List is empty
        if self.first == None:
            self.first = n
            self.last = n
        else:
            self.last.next = n
            self.last = n

    def print(self):
        #Print linked list items one by one
        n : Node = self.first

        while n:
            n.print()
            n = n.next

    def find(self, data):
        # Search in linked list by value
        n : Node = self.first

        while n:
            #Compare data with n.data
            if data == n.data:
                #Node has been found
                return n
            n = n.next

        #Node gas not been found
        return None

    def insert (self, m : Node, data):
        #Add node n behind m
        n : Node = Node(data)

        #Create links
        n.next = m.next
        m.next = n

    def delete (self, n : Node):
        #Next node
        m = n.next

        #Data copy
        n.data = m.data

        #Link
        n.next = m.next

        #Delete n
        m = None

class Stack:
    def __init__(self):
        self.first : Node = None
        self.last: Node = None

    def push (self, data):
        #Create new node
        n = Node(data)

        #List is empty
        if self.first == None:
            self.first = n
            self.last = n
        else:
            self.last.next = n
            n.prev = self.last
            self.last = n

    def print(self):
         # Print linked list items one by one
        n: Node = self.first

        while n:
            n.print()
            n = n.next

    def pop(self):
        #Stack is empty
        n = self.last

        if self.first == None:
            return

        #Stack has 1 element
        if self.first == self.last:
            self.first = None
            self.last = None

        #Stack has more elements
        else:
            self.last = n.prev
            self.last.next = None
            n = None


#Empty list
L = LList()
L.push('cartography')
L.push('gis')
L.push('remote sensing')
m = L.find('gis')
L.insert(m, 'python')
#L.print()
#m = L.find('remote sensing')
#L.delete(m)
#L.print()

S = Stack()
S.push('monday')
S.push('tuesday')
S.push('wednesday')
#S.print()
S.pop()
S.print()
