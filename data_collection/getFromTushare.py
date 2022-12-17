import requests
import tushare as ts
import pandas as pd


class GetData():

    def __init__(self, code, start_time, jiaoyisuo):
        self.code = code
        self.start = start_time
        self.getName(jiaoyisuo)
        self.ori_data = pd.DataFrame(ts.get_k_data(self.code, start=self.start))
        print(self.ori_data)
        self.save()

    def getName(self, jiaoyisuo):
        self.jiaoyisuo = jiaoyisuo
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42'
        }

        url = f'http://qt.gtimg.cn/q=s_{self.jiaoyisuo}600000'
        self.code_info_resp = requests.get(url, headers=headers)
        if self.code_info_resp.status_code == 200:
            print("股票名称查询成功")
        self.stocks_name = self.code_info_resp.text.split('~')[1]
        print(self.stocks_name)

    def save(self):
        self.ori_data.to_csv(f"../data/{self.stocks_name}.csv", encoding='utf8')


if __name__ == '__main__':
    code = '600000'
    start_time = '2005-05-05'
    exchange = 'sh'
    GetData(code, start_time, exchange)
