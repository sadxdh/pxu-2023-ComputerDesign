from data_collection import getFromTushare
from analytics import Resampling
import requests


def getName(code, exchange):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42'
    }
    url = f'http://qt.gtimg.cn/q=s_{exchange}{code}'
    code_info_resp = requests.get(url, headers=headers)
    if code_info_resp.status_code == 200:
        print("股票名称查询成功")
    stocks_name = code_info_resp.text.split('~')[1] + start_time
    print(stocks_name)
    return stocks_name


if __name__ == '__main__':
    code = '600000'
    start_time = '2005-05-05'
    exchange = 'sh'
    stock_name = getName(code, exchange)
    getFromTushare.GetData(code, start_time, exchange, stock_name)
    Resampling.Resampling(stock_name)
