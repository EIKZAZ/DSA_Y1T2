class Item:
    def __init__(self, name ,price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def getName(self):
        return self.name
    
    def getPrice(self):
        return self.price
    
    def getWeight(self):
        return self.weight
    
    def getCost(self):
        return self.price / self.weight
    
def knapsack(amount, itemList):
    itemList.sort(key=lambda x: x.getCost(), reverse=True)
    result = []
    total_value = 0
    remaining_weight = amount
    for item in itemList:
        if item.getWeight() <= remaining_weight:
            result.append(item)
            total_value += item.getPrice()
            remaining_weight -= item.getWeight()
    print(f"Knapsack Size: {amount} kg")
    print("=" * 30)
    for item in result:
        print(f"{item.getName()} -> {item.getWeight()} kg -> {item.getPrice()} THB")
    print(f"Total: {total_value} THB")

def main():
    item1 = Item('stereo', 3000, 3)
    item2 = Item('laptop', 2000, 2)
    item3 = Item('guitar', 1500, 1.5)
    itemList = [item1, item2, item3]
    knapsack(3.5, itemList)
    
    item1 = Item('tablet', 7000, 0.5)
    item2 = Item('perfume', 6000, 0.5)
    item3 = Item('guitar', 9000, 1)
    item4 = Item('air purifier', 9000, 2)
    item5= Item('watch', 8000, 0.5)
    itemList = [item1, item2, item3, item4, item5]
    knapsack(3, itemList)

main()
    
