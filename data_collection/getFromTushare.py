import os
import tushare as ts
import pandas as pd


class GetData:
    def __init__(self, code, start_time, jiaoyisuo, stock_name):
        self.code = code
        self.start = start_time
        self.jiaoyisuo = jiaoyisuo
        self.code_info_resp = None
        self.stocks_name = stock_name

        if not os.path.exists(f"data\\{self.stocks_name}.csv"):
            print("未在本地查询到数据。。")
            print("正在初始化数据。。")
            self.save()
        else:
            print("已获取到本地数据")
            self.ori_data = pd.read_csv(f"data\\{self.stocks_name}.csv")
            print(self.ori_data)

    def save(self):
        self.ori_data = pd.DataFrame(ts.get_k_data(self.code, start=self.start))
        print(self.ori_data)
        self.ori_data.to_csv(f"data\\{self.stocks_name}.csv", index=False, encoding='utf8')

    def delData(self):
        if not os.path.exists(f"data\\{self.stocks_name}.csv"):
            print("未在本地查询到数据文件")
        else:
            print(f"已获取到本地数据{self.stocks_name}.csv")
            print(f"{self.stocks_name}.csv 正在删除数据。。")
            self.ori_data = pd.read_csv(f"data\\{self.stocks_name}.csv")
            print(f"{self.stocks_name}.csv 文件删除完毕")


if __name__ == '__main__':
    code = '600000'
    start_time = '2005-05-05'
    exchange = 'sh'
    stock_name = "浦发银行2005-05-05"
    GetData(code, start_time, exchange, stock_name)
