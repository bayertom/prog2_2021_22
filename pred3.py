def insertSort(x : list[float]) ->list[float]:
    #Process all elements
    for i in range(len(x)):
        #Common element and its index
        j = i
        p = x[i]

        #Add element to the correct place
        while j > 0 and p < x[j-1]:
            #Swap x[j] and x[j-1]
            temp =  x[j]
            x[j] = x[j-1]
            x[j-1] = temp

            #Decrement index
            j = j - 1

def insertSort2(x : list[float]) ->list[float]:
    # Process all elements
    for i in range(len(x)):
        # Common element and its index
        j = i
        p = x[i]

        while  j > 0 and p < x[j-1]:
            #Move element right
            x[j] = x[j-1]

            #Decrement index
            j = j - 1

        #Write p to correct position
        x[j] = p

def bubbleSort(x : list[float]) ->list[float]: #Ascending order
    # Process all elements
    for i in range(len(x)):

        #From left to right
        for j in range (len(x) -1 ,i, -1):
            #Swap elements
            if x[j] < x[j-1]:
                temp = x[j]
                x[j] = x[j - 1]
                x[j - 1] = temp

def bubbleSort2(x : list[float]) ->list[float]: #Descending order
    # Process all elements
    for i in range(len(x)):
        print('.')

        #From left to right
        for j in range (0, len(x) - i - 1):
            #Swap elements
            if x[j] > x[j+1]:
                temp = x[j]
                x[j] = x[j + 1]
                x[j + 1] = temp


def bubbleSort3(x : list[float]) ->list[float]:
    # Assumption: x not sorted
    sorted = False

    while not(sorted):
        #Assumption: x is sorted
        sorted = True

        print('.')

        #From left to right
        i = 0
        for j in range (0, len(x) - i - 1):
            #Swap elements
            if x[j] > x[j+1]:
                temp = x[j]
                x[j] = x[j + 1]
                x[j + 1] = temp

                #x not sorted
                sorted = False
            i = i+1

def insertSort(x : list[float]) ->list[float]:
    # Process all elements
    for i in range(len(x)):

        #AInitialize minimum
        xmin = x[i]
        imin = i

        #Search for minimum
        for j in range(i, len(x)):

            #Actualize minimum
            if x[j] < xmin:
                xmin = x[j]
                imin = j
                
        #Swap elements
        temp = x[i]
        x[i] = x[imin]
        x[imin] = temp


x = [5 , -9, 38, 22, 24, 9, 1, 10 ]
selectSort(x)
bubbleSort(x)
insertSort(x)
print(x)