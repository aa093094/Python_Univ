from datascience import *
import numpy as np
import threading
import time

import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

# 랜덤 넘버 제너레이터 시작~~
np.random.seed(int(time.time()))
# np.random.seed(3)
Lotto_table = Table.read_table('Data_Science/Data/Lotto.CSV')
Sample = Lotto_table.take(make_array(np.random.randint(0, 1091)))
Lotto_1st_list = []
for i in range(1, 7):
  Lotto_data = Sample.column(i)
  Lotto_1st_list.append(Lotto_data[0])
index = Sample.column(0)[0]
print(index)
buyCount = Sample.column(10)[0].astype(int)
buyLottoList = []
count_1st = Sample.column(8)[0]
print(buyCount)
print(count_1st)
def sampling():
  for i in np.arange(buyCount):
    num_sel_temp = np.random.choice(a=45, size=6, replace=False)
    # 뽑은 6개 숫자 보정
    num_sel = [(b+1) for b in num_sel_temp]
    num_sel = sorted(num_sel)
    buyLottoList.append(num_sel)
sampling()
print(len(buyLottoList))
index = np.arange(1, buyCount+1, 1)
lotto = Table().with_columns(
    'Index', index,
    'Number', buyLottoList
    )
def win_lotto(lotto):
  for i in range(buyCount):
    if lotto == buyLottoList[i]:
      return 1
  return -1

def win_lotto_count(lotto):
  cnt = 0
  for i in range(buyCount):
    if lotto == buyLottoList[i]:
      cnt = cnt +1
  return cnt
print(win_lotto(Lotto_1st_list))
print(win_lotto_count(Lotto_1st_list))
