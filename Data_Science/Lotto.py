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
Sample = Lotto_table.take(make_array(np.random.randint(0, 1091)))
Lotto_table = ""
Lotto_1st_list = []
for i in range(1, 7):
  Lotto_data = Sample.column(i)
  Lotto_1st_list.append(Lotto_data[0])
index = Sample.column(0)[0]
print(index)
buyCount = Sample.column(10)[0].astype(int)
count_1st = Sample.column(8)[0]
print(buyCount)
print(count_1st)
win_cnt = 0
cnt = 0
current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%H:%M")

def win_lotto(win_cnt):
  if win_cnt > 0:
    return 1
  return -1

def win_lotto_count(num_sel, win_cnt, cnt):
  if Lotto_1st_list == num_sel:
    win_cnt = win_cnt +1
  cnt = cnt + 1
  if (cnt == (int)(buyCount/4)):
    print(cnt, formatted_time)
  elif (cnt == (int)(buyCount/4*2)):
    print(cnt, formatted_time)
  elif (cnt == (int)(buyCount/4*3)):
    print(cnt, formatted_time)

def sampling():
  for i in np.arange(buyCount):
    num_sel_temp = np.random.choice(a=45, size=6, replace=False)
    num_sel = [(b+1) for b in num_sel_temp]
    num_sel = sorted(num_sel)
    win_lotto_count(num_sel, win_cnt, cnt)
    num_sel = []

thread_list = []
print(cnt, formatted_time)
for i in range(10):
  thread = threading.Thread(target = sampling)
  thread_list.append(thread)
  thread.start()

for thread in thread_list:
  thread.join()

print(cnt)
print(win_lotto(win_cnt))
print(win_cnt)
