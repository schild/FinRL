import numpy as np


class QuantConnectEngineer:
    def __init__(self):
        pass

    def data_fetch(start_time, end_time, stock_list, resolution=Resolution.Daily):
        # resolution: Daily, Hour, Minute, Second
        qb = QuantBook()
        for stock in stock_list:
            qb.AddEquity(stock)
        return qb.History(qb.Securities.Keys, start_time, end_time, resolution)

    def preprocess(df, stock_list):
        df = df[["open", "high", "low", "close", "volume"]]
        if_first_time = True
        for stock in stock_list:
            if if_first_time:
                ary = df.loc[stock].values
                if_first_time = False
            else:
                temp = df.loc[stock].values
                ary = np.hstack((ary, temp))
        return ary
