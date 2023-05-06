def coinExchange(amount,coinList):
    coin = [10,5,2,1]
    count_coin = [0,0,0,0]
    total = 0
    a = amount
    for i in range(len(coin)):
        while amount >= coin[i] and coinList[i] > 0:
            amount -= coin[i]
            coinList[i] -= 1
            count_coin[i] += 1
            total += 1
    if amount > 0:
        print("Amount:", a)
        print("Coins are not Enough.")
    else:
        print("Amount:", a)
        print("Coin exchange result:", count_coin)
        print("Number of coins:", total)

def main():
    coinList = [10, 10, 10, 10]
    coinExchange(127, coinList)
    print("---------------------")
    coinExchange(249, coinList)
main()
