def cardData(list):
    special = ["J", "Q", "K", "A"]
    sign = ["♣", "♦", "♥", "♠"]
    for i in range(len(list)):
        list[i] = list[i].replace(list[i][-1], str(sign.index(list[i][-1])))
        if(list[i][0] in special):
            list[i] = (str(11 + int(special.index(list[i][0]))) + list[i][1:])
        list[i] = int(list[i])
    return list

def insertionSort(list, last):
    first_list = list.copy()
    list = cardData(list)
    current = 1
    compare = 0
    while (current <= last):
        hold = list[current]
        hold2 = first_list[current]
        walker = current-1
        compare +=1
        while (walker >= 0 and hold < list[walker]):
            list[walker+1] = list[walker]
            first_list[walker+1] = first_list[walker]
            walker -= 1
            compare += 1
        list[walker+1] = hold
        first_list[walker+1] = hold2
        current += 1
        if (walker < 0):
            compare -= 1
        print(first_list)
    print("Comparison times:",compare)

def selectionSort(list, last):
    first_list = list.copy()
    list = cardData(list)
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
        first_list[current],first_list[smallest] = first_list[smallest],first_list[current]
        current += 1
        print(first_list)
    print("Comparison times:",compare)

def bubbleSort(list, last):
    first_list = list.copy()
    list = cardData(list)
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
                first_list[walker],first_list[walker -1] = first_list[walker -1],first_list[walker]
            walker -= 1
        current += 1
        print(first_list)
    print("Comparison times:",compare)

insertionSort(['4♣', 'A♣', '10♥', 'K♦', '4♠', '10♣', '3♦', '7♥', '4♦','4♣','4♣','3♦','2♦'], 12)
print("-----------------------------------------------------------------")
selectionSort(['4♣', 'A♣', '10♥', 'K♦', '4♠', '10♣', '3♦', '7♥', '4♦','4♣','4♣','3♦','2♦'], 12)
print("-----------------------------------------------------------------")
bubbleSort(['4♣', 'A♣', '10♥', 'K♦', '4♠', '10♣', '3♦', '7♥', '4♦','4♣','4♣','3♦','2♦'], 12)
