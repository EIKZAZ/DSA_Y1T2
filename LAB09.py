def insertionSort(list, last):
    current = 1
    compare = 0
    while (current <= last):
        hold = list[current]
        walker = current-1
        while (walker >= 0 and hold < list[walker]):
            list[walker+1] = list[walker]
            walker -= 1
            compare += 1
        list[walker+1] = hold
        current += 1
        if (walker < 0):
            compare -= 1
        print(list)
    print("Comparison times:",compare)

def selectionSort(list, last):
    current = 0
    compare = 0
    while (current < last):
        smallest = current
        walker = current + 1
        while (walker <= last):
            compare += 1
            if (list[walker] < list[smallest]): 
                smallest = walker
            walker += 1
        list[current],list[smallest] = list[smallest],list[current]
        current += 1
        print(list)
    print("Comparison times:",compare)

def bubbleSort(list, last):
    current = 0
    compare = 0
    sorted = False
    while(current <= last and sorted is False):
        walker = last
        sorted = True
        while(walker > current):
            compare += 1
            if (list[walker] < list[walker-1]):
                sorted = False
                list[walker],list[walker -1] = list[walker -1],list[walker]
            walker -= 1
        current += 1
        print(list)
    print("Comparison times:",compare)


insertionSort([32, 87, 45, 8, 32, 56, -1, 0], 7)
print("-----------------------------------")
selectionSort([32, 87, 45, 8, 32, 56, -1 ,0], 7)
print("-----------------------------------")
bubbleSort([32, 87, 45, 8, 32, 56, -1, 0], 7)

