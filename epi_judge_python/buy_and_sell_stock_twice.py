from test_framework import generic_test

def first(prices):

    current_index, last_index = 1, len(prices) - 1
    current_profit, profit = 0.0, 0.0
    second_largest_profit, largest_profit = 0.0, 0.0

    while current_index <= last_index:
        current_profit += prices[current_index] - prices[current_index - 1]
        if current_profit > profit:
            profit = current_profit
        if current_profit < 0:
            current_profit = 0.0
            if profit > largest_profit:
                largest_profit, second_largest_profit = profit, largest_profit
            elif profit > second_largest_profit:
                second_largest_profit = profit
            print("\n", current_index, prices[current_index], profit, largest_profit, second_largest_profit)
            profit = 0.0
        current_index += 1

    if profit > largest_profit:
        largest_profit, second_largest_profit = profit, largest_profit
    elif profit > second_largest_profit:
        second_largest_profit = profit

    return largest_profit + second_largest_profit

def buy_and_sell_stock_twice(prices):
    return first(prices)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock_twice.py",
                                       "buy_and_sell_stock_twice.tsv",
                                       buy_and_sell_stock_twice))
