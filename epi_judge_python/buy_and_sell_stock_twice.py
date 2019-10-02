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
            # print("\n", current_index, prices[current_index], profit, largest_profit, second_largest_profit)
            profit = 0.0
        current_index += 1

    if profit > largest_profit:
        largest_profit, second_largest_profit = profit, largest_profit
    elif profit > second_largest_profit:
        second_largest_profit = profit

    return largest_profit + second_largest_profit

def second(prices):

    if not prices:
        return 0.0

    current, last = 1, len(prices) - 1
    low, high = [0, 0], [0, 0]
    current_low = 0

    while current <= last:
        if prices[current] < prices[current_low]:
            current_low = current
        if prices[current] > prices[current_low]:
            if low[0] == 0 or low[0] == current_low:
                low[0] = current_low
                high[0] = current
            elif low[1] == 0 or low[1] == current_low:
                low[1] = current_low
                high[1] = current
            else:
                sd = min(prices[high[0]] - prices[low[1]], prices[high[1]] - prices[current_low])
                if prices[current] - prices[current_low] > sd:
                    if prices[high[0]] - prices[low[1]] < prices[high[1]] - prices[current_low]:
                        high[0] = high[1]
                        low[1] = current_low
                        high[1] = current
                    else:
                        high[1] = current
                        current_low = high[1]
        current += 1

    print('\n', high[0], low[0], prices[high[0]], prices[low[0]])
    print('\n', high[1], low[1], prices[high[1]], prices[low[1]])
    return (prices[high[0]] - prices[low[0]]) + (prices[high[1]] - prices[low[1]])

def buy_and_sell_stock_twice(prices):
    # return first(prices)
    return second(prices)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock_twice.py",
                                       "buy_and_sell_stock_twice.tsv",
                                       buy_and_sell_stock_twice))
