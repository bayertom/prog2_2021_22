class TNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def preoder(self, u):
        if u == None:
            return
        else:
            print(u.data)
            self.preoder(u.left)
            self.preoder(u.right)

    def insert(self, u, data):
        if u == None:
            u = TNode(data)
        else:
            if data < u.data:
                u.left = self.insert(u.left, data)
            elif data > u.data:
                u.right = self.insert(u.right, data)
            else:
                return None
        return u

    def insertNode(self, data):
        self.root = self.insert(self.root, data)
        return self.root

    def Print(self):
        self.preoder(self.root)

    def find(self, data, u):
        if u == None:
            return None
        if data == u.data:
            return u
        if data < u.data:
            return self.find(data, u.left)
        else:
            return self.find(data, u.right)

    def findNode(self, data):
        return self.find(data, self.root)

    def clear(self, u):
        if u != None:
            self.clear(u.left)
            self.clear(u.right)
            u = None


bst = BST()
bst.insertNode(15)
bst.insertNode(13)
bst.insertNode(25)
bst.Print()

u = bst.findNode(25)
if u != None:
    print(u.data)
    print(p[0].data)
else:
    print('Not found')

