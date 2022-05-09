class PQItem:
    def __init__(self, priority, item):
        self.priority = priority
        self.item = item

class PQ:
    def __init__(self, n_max):
        self.n = 0
        self.h = [PQItem(0, 0)] * (n_max +1)

    def print(self):
        for i in range(1, self.n+1):
            print(self.h[i].priority, self.h[i].item)

    def fhu(self, i):
        # Fix heap up
        while i > 1 and self.h[i // 2].priority < self.h[i].priority:
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
            if k < self.n and self.h[k+1].priority > self.h[k].priority:
                k = k + 1

            #Swap elements
            if self.h[i].priority < self.h[k].priority:
                temp = self.h[i]
                self.h[i] = self.h[k]
                self.h[k] = temp

            #Stop
            else:
                break

            #Go to parent
            i = k

    def push (self, priority, item):
        #Add element to heap
        self.n = self.n + 1
        self.h[self.n] = PQItem(priority, item)

        #Fix heap up
        self.fhu(self.n)


    def pop(self):
        #Delete root
        temp = self.h[1]
        self.h[1] = self.h[self.n]
        self.h[self.n] = temp

        #Shorter heap
        self.n = self.n - 1

        #Fix heap down
        self.fhd(1)

#Priority queue
pq = PQ(10)

#Add 3 points with given priority
pq.push(1, [10, 10])
pq.push(10, [15, 15])
pq.push(13, [13, 13])

#Remove points according to their priority
pq.print()
pq.pop()
pq.print()
pq.pop()
pq.print()
pq.pop()
pq.print()