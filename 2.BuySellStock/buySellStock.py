'''
provided sol:
t: 1419 ms
m: 22.6 MB
'''
def maxProfitSol(prices):
    l, r = 0, 1
    maxP = 0
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
        else:
            l = r
        r += 1
    
    return maxP


'''
blind run
t: 884 ms
m: 22.7 MB
'''
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    highest_profit = 0
    low = prices[0]
    high = prices[0]
    for p in prices[1:]:
        if p < low:
            # found a new global min; store previous profit if it is higher than previous
            profit = high - low
            if profit > highest_profit:
                highest_profit = profit
            low = p
            high = p
            
        elif p > high:
            high = p

    # confirm the last high low
    profit = high - low
    if profit > highest_profit:
        highest_profit = profit    
    return highest_profit

if __name__ == '__main__':
    prices = [2,4,1]
    print(maxProfit(prices))