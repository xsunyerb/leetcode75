def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit

prices = [7,1,5,3,6,4]
# Output: 5
result = maxProfit(prices)
print(result)

prices = [7,6,4,3,1]
# Output: 0
result = maxProfit(prices)
print(result)