def maxProfit(prices):
    minprice = 10 ** 5
    price = 0
    for i in prices:
        price = max(price, i - minprice)
        minprice = min(minprice, i)
    return price


if __name__ == "__main__":
    arr = [int(x) for x in input("Enter Array : ").split()]
    print(maxProfit(arr))
