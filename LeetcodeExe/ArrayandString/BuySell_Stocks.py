def Solution (self):
    price = [7,10, 1,2,4]
    max_price = 0
    min_price = price[0]

    if len(price) == 0:
        return 0

    for i in range(len(price)):

        if price[i] < min_price:
            min_price = price[i]

        profit = price[i] - min_price

        if profit > max_price:
            max_price = profit

    print(max_price)

Solution(None)








