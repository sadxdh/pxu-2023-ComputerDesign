# 股票分析与模型预测



## 最终目标：

全自动化部分：数据获取，数据处理，数据分析，数据展示，数据格式化、模型训练、模型预测、买卖标注

半自动化部分：模型选取（根据数据具体分布，提示模型选择）

手动部分：股票选择，股票买卖



## 数据来源：

网页爬取，财经库（要求实时数据）



## 技术需求：

Python基础，python分析（pandas，numpy），可视化（matplotlib），机器学习（sklearn）



## 项目主体实现步骤：

1、获取数据--》爬虫、调用财经库接口

- 例（下文同例）：
- 利用yfinance库，下载下列股票数据，然后进行一系列分析 
  1. 英特尔公司股票 （代码为'INTC')
  2. 美国标准普尔500指数 （代码为'^GSPC')

- 下载股票每天价格信息（定义1/1/2000到5/31/2022为整个时间段），并把时间序列画图演示。用三句话描述你从标准普尔500指数中观察到的最重要信息。

2、数据预处理--》数据清洗（除杂、去重、不合理数据增删改等）

3、数据分析--》特征值提取（增长率、峰值等）--》数据可视化

- 计算它们每天的百分比变化，并把其时间序列画图演示。简单谈谈从美国标准普尔500的变化中观察到什么？（如果有人说股票市场的波动率本身，波动很大，你同意吗？）

4、数据挖掘--》在数据分析的基础上挖掘高价值信息（入仓出仓、资本增幅率、风险管控）

- 首先根据整个时间段（1/1/2000--5/31/2022）计算上述变量，然后对疫情期间（1/1/2020--5/31/2022）重复以上计算。
- 美国标准普尔500指数通常用来代表整个美国市场，以此假设计算英特尔公司的Beta值（利用每个月的调整收盘价'Adj Close'，类似课堂案例），并且比较整个时间段和疫情期间的差别
- 根据你的计算结果，英特尔公司股票的系统性风险跟整个市场（美国标准普尔500指数）相比是高还是低？你期望的回报率应该高于还是低于市场回报率？
- 假设投资者考虑一个简单投资组合，在英特尔和标准普尔500之间进行资产配置。根据整个时间段期间的年化回报率和波动率以及相关系数， 计算并画示投资组合的回报率（纵坐标）和标准差（波动率，横坐标）随配比比重（变量w)变化曲线，计算投资组合最小方差的最优配比。
- 对于美国标准普尔500指数进行蒙特卡洛模拟（价格百分比变化假设为正态分布），并图示在各场景中价格如何随时间变化。要求如下：
  - S0： 起始价格或者指数值，利用5/31/2022调整收盘价
  - T： 预报时间段，年， 2年
  - mu： 预期未来年化回报率，自我假设，建议在-0.3和0.3之间选取
  - sigma：预期未来波动率，使用疫情期间计算的波动率
  - numS： 场景数，不同场景个数，建议1000
  - numT： 总步数，建议200
- 利用假设的波动率，计算指数变化百分比在以下时间之后的理论标准差 （1）半年，（2）一年， （3）两年。请与上图对比，看看是否吻合（是或者不是）

5、机器学习训练模型（通过大量的数据集训练股票走势模型）

- 提供模型测试分数，挑出各项数据得分较高的模型

6、通过模型提供预测对新增数据集提供发展趋势

- 实时预测


## 补充项目：

网络编程：要求实现客户端与服务器交互

页面设计：终端界面设计（手机端或电脑端、服务器端）

 

## 交互方式：

终端--》服务器--》终端



 ## 案例样本：

### 网页样本数据：

[数据中心 _ 东方财富网 (eastmoney.com)](https://data.eastmoney.com/center/)



 ## 技术教程：

### 数据集样本：

[农业银行 2.85 (1.06%) (601288)_个股行情_网易财经 (163.com)](http://quotes.money.163.com/trade/cjmx_601288.html)

 

### Python基础：

[Python基础教程，Python入门教程（非常详细） (biancheng.net)](http://c.biancheng.net/python/)



### 机器学习：

[吴孟达_coursera_machine-learning_无字幕无翻译](https://www.coursera.org/learn/machine-learning)

[吴孟达bilibili_machine-learning中英字幕](https://www.bilibili.com/video/BV1Pa411X76s)
