# python 实现对纳斯达克指数定投收益计算
import pandas as pd
import random
from datetime import datetime,timedelta

# 带千分位字符串转浮点数
def str_to_float(s):
  return float(s.replace(',', ''))

# 计算出每日固定投入，计算出区间收益
# 输入：开始日期xxxx/xx/xx，和时间跨度（几年），定投金额
# 输出：定投后总金额，定投总成本，定投利润
def fixed_calculate_profit(start_date, time_span, invest_amount):
  # df = pd.read_csv("./files/allDate.csv")
  # 获取开始日期之前的交易日数据
  df = pd.read_csv("./files/allDate.csv")
  end_date = str(int(start_date.split('/')[0]) + int(time_span)) + '/' + start_date.split('/')[1] + '/' + start_date.split('/')[2]
  df = df[(df['日期'] >= start_date) & (df['日期'] < end_date)]
  rows, columns  = df.shape
  end = df.iloc[0]
  endprice = end['收盘']
  profit_sum = 0
  # 总投入成本
  total_cost = invest_amount * rows
  # 倒序遍历2024年交易日数据，计算每天的收益  
  for i in range(rows - 1, -1, -1):
    current_row = df.iloc[i]
    current_price = current_row['收盘']
    current_profit = invest_amount + (str_to_float(endprice) - str_to_float(current_price)) / str_to_float(current_price) * invest_amount
    profit_sum += current_profit

  result = {
    'date_range': start_date + '-' + end_date,
    'row_counts': rows,
    'total_cost': total_cost,
    'total_revenue': profit_sum - total_cost,
    'profit_sum': profit_sum
  }
  return result
  print(f'{start_date} - {end_date}定投后总金额：', profit_sum)
  print(f'{start_date} - {end_date}定投成本总金额：', total_cost)
  print(f'{start_date} - {end_date}定投收益额：', profit_sum - total_cost)

# fixed_calculate_profit('2021/01/01', 4, 200)

# 计算随机起始日期[1986年，]，固定时间跨度，固定定投金额，计算收益的分布，即随机调用fixed_calculate_profit函数
# 输入：随机次数，开始日期范围，时间跨度，定投金额
# 输出：定投后总金额，定投总成本，定投利润
# def random_start_date_calculate_profit(random_count, start_date_range, time_span, invest_amount):
  # profit_list = []
  # for i in range(random_count):
    
# 随机生成日期范围内的起始日期
def random_start_date(start_year, end_year):
  year = random.randint(start_year, end_year)
  month = random.randint(1, 12)
  first_day_month = datetime(year, month, 1)
  if month == 12:
    first_day_next_month = datetime(year+1, 1, 1)
  else:
    first_day_next_month = datetime(year, month + 1, 1)
  last_day_month = first_day_next_month - timedelta(days=1)
  days_in_month = last_day_month.day
  day = random.randint(1, days_in_month)
  random_date = datetime(year,month,day)
  return random_date


def random_start_date_group_investment():
  date_group = []
  date_length = 10
  random_start = 2010
  random_end = 2020
  for i in range(date_length):
    prdate = random_start_date(random_start, random_end).strftime('%Y/%m/%d')
    date_group.append(prdate)

  for item in date_group:
    fixed_calculate_profit(item, 5, 100)

# random_start_date_group_investment()
result = fixed_calculate_profit('2010/01/01', 5, 100)
print(result)


## 就从最早的年份开始，5年收益分布