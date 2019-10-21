from test_framework import generic_test

def first(prices):
    
    current_profit, profit = 0.0, 0.0
    current_index, last_index = 1, len(prices) - 1

    while current_index <= last_index:
        current_profit += prices[current_index] - prices[current_index - 1]
        if current_profit > profit:
            profit = current_profit
        if current_profit < 0:
            current_profit = 0.0
        current_index += 1

    return profit

def second(prices):
    
    if not prices:
        return 0.0

    current, last = 1, len(prices) - 1
    lowest_value, profit = prices[0], 0.0

    # loop over the list
    # always remember the lowest value seen so far, keep record for current profit
    # whenever see a bigger value, minus the lowest to see if can get more profit
    # whenever see a smaller value, compare with lowest to determin current lowest
    while current <= last:
        if prices[current] < prices[current - 1]:
            lowest_value = min(lowest_value, prices[current])
        if prices[current] > prices[current - 1]:
            profit = max(profit, prices[current] - lowest_value)
        current += 1

    return profit

def buy_and_sell_stock_once(prices):
    # return first(prices)
    return second(prices)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
