def quickSort(x : list[float], l : int, r : int) ->list[float]:
    #Left and right indices
    i = l
    j = r

    #Pivot, mid element
    p = x[(l+r)//2]

    #Swap incorrect items according to pivot
    while i <= j:
        #Item larger than pivot in the left part
        while x[i] < p:
            i = i + 1
        # Item smaller than pivot in the right part
        while x[j] > p:
            j = j - 1

        #Swap items
        if i <= j:
            temp = x[i]
            x[i] = x[j]
            x[j] = temp
            i = i + 1
            j = j - 1

    #Recursion, left part
    if j > l:
        quickSort(x, l, j)

    # Recursion, right part
    if i < r:
        quickSort(x, i, r)

def mergeSort(x: list[float], l: int, r: int) -> list[float]:

    #Mid index
    m = (l + r) // 2

    #Stop recursion
    if l==r:
        return

    #Recursion, left interval
    mergeSort(x, l, m)

    #Recursion, right interval
    mergeSort(x, m+1, r)

    #Merge both parts
    merge (x, l, m, r)

def merge(x, l, m, r):
    #Auxiliry lists
    a = x[l:m+1]
    b = x[m+1:r + 1]

    #Initialize indices
    i = 0
    j = 0
    n = len(a)
    m = len(b)

    #Merge procedure
    for k in range(l, r + 1):

        # We reach end of the first sequence
        if i == n:
            x[k] = b[j]
            j = j + 1
            continue

        # We reach end of the second sequence
        if j == m:
            x[k] = a[i]
            i = i + 1
            continue

        # a is smaller
        if a[i] < b[j]:
            x[k] = a[i]
            i = i + 1

        # b is smaller
        else:
            x[k] = b[j]
            j = j + 1

def heapSort(x):
    n = len(x);
    h = [0]*(n+1)

    #Create new heap
    for i in range(n):
        h[i+1] = x[i]
        fhu(h, i + 1)

    #Sorting procedure
    while (n > 1):
        #Switch h[1] <=> h[n]
        temp = h[1]
        h[1] = h[n]
        h[n] = temp

        #Decrease the heap length
        n = n - 1

        #Correct the heap from the root
        fhd(h,1,n)
        
    #Elements in reversed order
    print(h)

def fhu(h, i):
    #Fix heap up
    while i > 1 and h[i//2] > h[i]:
        temp = h[i//2]
        h[i//2] = h[i]
        h[i] = temp
        i = i//2

def fhd(h, i, n):
    #Fix heap down
    while 2 * i<= n:
        #Initialize as the left child
        k = 2 * i

        #Switch to right child
        if k < n and h[k+1] < h[k]:
            k = k + 1

        #Swap items, if necsessary
        if h[i] > h[k]:
            temp = h[i]
            h[i] = h[k]
            h[k] = temp

        #Stop fixing
        else:
            break

        #Contonue with a child
        i = k


x = [5 , -9, 38, 22, 24, 9, 1, 10 ]
#quickSort(x, 0, len(x)-1)
#mergeSort(x, 0, len(x)-1)
heapSort(x)
print(x)