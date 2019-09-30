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

def buy_and_sell_stock_once(prices):
    return first(prices)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
