from datascience import *
import numpy as np
import threading
import time
import datetime

import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

np.random.seed(int(time.time()))
# np.random.seed(3)
Lotto_table = Table.read_table('Data_Science/Data/Lotto.CSV')
reversed_table = Lotto_table.sort('회차')
number = np.random.randint(0, 100)
num_list = []
if (number > 90):
  for i in range(0, 10):
    temp = number + 100 * i
    num_list.append(temp)
  num_list.append(1090)
else:
  for i in range(0, 11):
    temp = number + 100 * i
    num_list.append(temp)
Sample_list = []
for nums in num_list:
  Sample = reversed_table.take(make_array(nums))
  Sample_list.append(Sample)
Lotto_table = ""
reversed_table = ""
num_list = []
index_list = []
real_win_cnt_list = []
sample_win_cnt_list = []
buyCount_list = []

def sampling(Count):
  global cnt
  global win_cnt
  for i in np.arange(Count):
    num_sel_temp = np.random.choice(a=45, size=6, replace=False)
    num_sel = [(b+1) for b in num_sel_temp]
    num_sel = sorted(num_sel)
    if (Lotto_1st_list == num_sel):
      win_cnt = win_cnt + 1
    num_sel = []
    cnt = cnt + 1
    if (cnt % 10000000 == 0):
      current_time = datetime.datetime.now()
      formatted_time = current_time.strftime("%H:%M")
      print(win_cnt, cnt, formatted_time)

for r in range(10):
  for j in range(0, 11):
    Lotto_1st_list = []
    for i in range(1, 7):
      Lotto_data = Sample_list[j].column(i)
      Lotto_1st_list.append(Lotto_data[0])
    index = Sample_list[j].column(0)[0]
    print(index)
    index_list.append(index)
    buyCount = Sample_list[j].column(10)[0].astype(int)
    count_1st = Sample_list[j].column(8)[0]
    print(buyCount)
    print(count_1st)
    buyCount_list.append(buyCount)
    real_win_cnt_list.append(count_1st)
    win_cnt = 0
    cnt = 0
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%H:%M")
        
    thread_list = []
    print(cnt, formatted_time)
    np.random.seed(int(time.time()))
    for i in range(2000):
      thread = threading.Thread(target = sampling(buyCount/2000))
      thread_list.append(thread)
      thread.start()

    for thread in thread_list:
      thread.join()

    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%H:%M")
    print(win_cnt, cnt, formatted_time)
    sample_win_cnt_list.append(win_cnt)

  All_table = Table().with_columns(
    'index', index_list,
    'Real_win', real_win_cnt_list,
    'Total_cnt', buyCount_list,
    'Sample_win', sample_win_cnt_list
  )

  All_table.to_csv('Lotto_Sampling' + str(r) + '.csv')
  All_table = ""





