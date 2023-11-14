from datascience import *
import numpy as np

import matplotlib.pyplot as plots
import matplotlib
matplotlib.use('TkAgg')
plots.style.use('fivethirtyeight')

Lotto_table = Table.read_table('Data_Science/Data/Lotto.CSV')
reversed_table = Lotto_table.sort('회차')
win_cnt_list = reversed_table.column(8)
buyCount_list = reversed_table.column(10).astype(int)
index_list = reversed_table.column(0)
Lotto_table = ""
reversed_table = ""

Sample_list0 = []
Sample_list1 = []
Sample_list2 = []
Sample_list3 = []
Sample_list4 = []
Sample_list5 = []
Sample_list6 = []
Sample_list7 = []
Sample_list8 = []
Sample_list9 = []
Sample_list10 = []

for i in range(3):
    Sample_Table = Table.read_table('Data_Science/Data/Lotto_Sampling' + str(i) + '.csv')
    Win_Data = Sample_Table.column(3)
    Sample_list0.append(Win_Data[0])
    Sample_list1.append(Win_Data[1])
    Sample_list2.append(Win_Data[2])
    Sample_list3.append(Win_Data[3])
    Sample_list4.append(Win_Data[4])
    Sample_list5.append(Win_Data[5])
    Sample_list6.append(Win_Data[6])
    Sample_list7.append(Win_Data[7])
    Sample_list8.append(Win_Data[8])
    Sample_list9.append(Win_Data[9])
    Sample_list10.append(Win_Data[10])

sum = 0
for cnt in win_cnt_list:
    sum = sum + cnt
avg = sum / len(win_cnt_list)
print(avg)

win_cnt_table = Table().with_columns(
    'index', index_list,
    'win_cnt', win_cnt_list
)

buyCount_table = Table().with_columns(
    'index', index_list,
    'buyCount', buyCount_list
)

win_cnt_table.plot('index', 'win_cnt', linewidth = 0.5)
plots.xlabel('Index')
plots.ylabel('Win_Cnt')
plots.title('Win_Cnt_Table')
plots.show()

buyCount_table.plot('index', 'buyCount', linewidth = 0.5)
plots.xlabel('Index')
plots.ylabel('BuyCount')
plots.title('BuyCount_Table')
plots.show()








