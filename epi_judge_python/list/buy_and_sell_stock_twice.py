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

def third(prices):

    if not prices:
        return 0.0

    current, last = 1, len(prices) - 1
    buy1, sell1, buy2, sell2 = 0, 0, 0, 0
    current_low_index, current_low_value = 0, float('inf')

    while current <= last:
        if prices[current] > prices[current - 1]:
            if buy1 == sell1:
                buy1 = current - 1
                sell1 = current
                current_low_index = current
                current_low_value = prices[current]
            elif sell1 == current - 1:
                sell1 = current
                current_low_index = current
                current_low_value = prices[current]
            elif buy2 == sell2:
                buy2 = current - 1
                sell2 = current
                current_low_index = current
                current_low_value = prices[current]
            elif sell2 == current - 1:
                sell2 = current
                current_low_index = current
                current_low_value = prices[current]
            else:
                current_profit = prices[current] - prices[current_low_index]
                sd = min(
                    prices[sell1] - prices[buy1],
                    prices[sell2] - prices[buy2],
                    prices[sell1] - prices[buy2],
                    prices[sell2] - prices[current_low_index],
                    current_profit
                )
                if current_profit > sd:
                    if prices[sell1] - prices[buy1] == sd:
                        buy1 = buy2
                        sell1 = sell2
                        buy2 = current_low_index
                        sell2 = current
                    elif prices[sell2] - prices[buy2] == sd:
                        buy2 = current_low_index
                        sell2 = current
                    elif prices[sell1] - prices[buy2] == sd:
                        sell1 = sell2
                        buy2 = current_low_index
                        sell2 = current
                    elif prices[sell2] - prices[current_low_index] == sd:
                        sell2 = current
                    current_low_index = current
                    current_low_value = prices[current]
        elif prices[current] < prices[current - 1]:
            if prices[current] < current_low_value:
                current_low_index = current
                current_low_value = prices[current]

        current += 1    

    return (prices[sell1] - prices[buy1]) + (prices[sell2] - prices[buy2])

def second(prices):

    if not prices:
        return 0.0

    current, last = 1, len(prices) - 1
    low, high = [0, 0], [0, 0]
    current_low = 0
    print(prices)
    while current <= last:
        if prices[current] < prices[current_low]:
            current_low = current
        if prices[current] > prices[current_low]:
            if low[0] == high[0] or low[0] == current_low:
                low[0] = current_low
                high[0] = current
            elif low[1] == high[1] or low[1] == current_low:
                low[1] = current_low
                high[1] = current
            else:
                sd = min(
                        prices[high[0]] - prices[low[0]],
                        prices[high[1]] - prices[low[1]],
                        prices[current] - prices[current_low],
                        prices[high[0]] - prices[low[1]],
                        prices[high[1]] - prices[current_low]                        
                    )
                if sd < prices[current] - prices[current_low]:
                    if sd == prices[high[0]] - prices[low[0]]:
                        low[0] = low[1]
                        high[0] = high[1]
                        low[1] = current_low
                        high[1] = current
                    elif sd == prices[high[1]] - prices[low[1]]:
                        low[1] = current_low
                        high[1] = current
                    elif sd == prices[high[0]] - prices[low[1]]:
                        high[0] = high[1]
                        low[1] = current_low
                        high[1] = current
                    elif sd == prices[high[1]] - prices[current_low]:
                        high[1] = current
                        current_low = current
        print('\ncurrent = ', current, ' current value = ', prices[current], ' current low value = ', prices[current_low])
        print('\t', low[0], high[0], prices[low[0]], prices[high[0]])
        print('\t', low[1], high[1], prices[low[1]], prices[high[1]])

        current += 1

    return (prices[high[0]] - prices[low[0]]) + (prices[high[1]] - prices[low[1]])

def buy_and_sell_stock_twice(prices):
    # return first(prices)
    # return second(prices)
    return third(prices)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock_twice.py",
                                       "buy_and_sell_stock_twice.tsv",
                                       buy_and_sell_stock_twice))
