#answering the question here: https://app.interviewquery.com/questions/buy-or-sell
stock_prices = [32,10,9,20,25,5]
dts = [
    '2019-01-01',
    '2019-01-02',
    '2019-01-03',
    '2019-01-04',
    '2019-01-05',
    '2019-01-06']

def get_max_profit(stock_prices,dts):
    prof = 0
    ind = []
    for i,j in enumerate(stock_prices):
        rest = stock_prices[i+1 :]
        for f, k in enumerate(rest):
            if k - j > prof:
                prof = k-j
                ind = [i, i+f+1]
    print(prof,dts[ind[0]],dts[ind[1]])

get_max_profit(stock_prices,dts)
