class Heap:
    def __init__(self, n_max):
        self.n = 0
        self.h = [0] * (n_max +1)

    def print(self):
        print(self.h)

    def fhu(self, i):
        # Fix heap up
        while i > 1 and self.h[i // 2] > self.h[i]:
            #Swap elements
            temp = self.h[i // 2]
            self.h[i // 2] = self.h[i]
            self.h[i] = temp

            #Go to parent
            i = i // 2

    def fhd(self, i):
        # Fix heap down
        while 2*i <= self.n:
            #Left child
            k = 2 * i

            #Right child is smaller
            if k < self.n and self.h[k+1] < self.h[k]:
                k = k + 1

            #Swap elements
            if self.h[i] > self.h[k]:
                temp = self.h[i]
                self.h[i] = self.h[k]
                self.h[k] = temp

            #Stop
            else:
                break

            #Go to parent
            i = k

    def add (self, item):
        #Add element to heap
        self.n = self.n + 1
        self.h[self.n] = item

        #Fix heap up
        self.fhu(self.n)

    def min(self):
        #Fond minimum
        return self.h[1]

    def max(self):
        #Find maximum
        max_el = self.h[self.n//2]

        #Traverse only leaves
        for i in range(self.n//2, self.n+1):
            if self.h[i] > max_el:
                max_el = self.h[i]
        return max_el

    def delRoot(self):
        #Delete root
        temp = self.h[1]
        self.h[1] = self.h[self.n]
        self.h[self.n] = temp

        #Shorter heap
        self.n = self.n - 1

        #Fix heap down
        self.fhd(1)

    def heapSort(self, X):
        #Create heap sort
        for x in X:
            self.add(x)
        ns = self.n

        #Remove root
        while self.n >= 1:
            self.delRoot()

        return self.h[1:ns+1]

#Double linked node
class Node2:
    def __init__(self, data):
        self.data = data
        self.prev: Node2 = None
        self.next : Node2 =  None

    def print(self):
        print(self.data)

#Implement PQ using Doubly Linked List
class PriorityQueue:
    def __init__(self):
        self.first : Node2 = None
        self.last: Node2 = None

    def push (self, data):
        #Create new node
        n = Node(data)

        #PQ is empty
        if self.first == None:
            self.first = n
            self.last = n
        else:
            self.last.next = n
            n.prev = self.last
            self.last = n

heap = Heap(15)
heap.add(3)
heap.add(15)
heap.add(-1)
heap.add(-11)


#heap.print()
#print(heap.min())
#print(heap.max())
heap.print()
heap.delRoot()
heap.print()
heap.delRoot()
heap.print()
heap.delRoot()
heap.print()
heap.delRoot()
X = [ 1 , 6, 4, 8, 31, 3, 2022]
XS = heap.heapSort(X)
print(XS)