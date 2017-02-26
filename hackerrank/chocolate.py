def maxChocolate(money, price, wrap):
    if (money < price):
        return
    bought = int(money / price)

    bought = bought + (bought - 1) / (wrap - 1)
    return bought

print(maxChocolate(16, 2, 2))

# maxChocolate(15, 1, 3)
