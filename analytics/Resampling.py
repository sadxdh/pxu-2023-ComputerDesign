import pandas as pd
import matplotlib.pyplot as plt


class Resampling:
    def __init__(self, filename):
        self.filename = filename
        self.stock_week = None
        self.stock_train = None
        self.data = pd.read_csv(f"data\\{self.filename}.csv", index_col=0, parse_dates=[0])
        print(self.data)
        self.resamplingWeek()
        self.draw()

    def resamplingWeek(self):
        self.stock_week = self.data['close'].resample('W').mean()
        print(self.stock_week)
        self.stock_train = self.stock_week['2005':'2017'].dropna()
        print(self.stock_train)

    def draw(self):
        self.stock_train.plot()
        plt.show()


if __name__ == '__main__':
    filename = "浦发银行2005-05-05"
    Resampling(filename)
