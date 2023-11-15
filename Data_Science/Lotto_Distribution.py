from datascience import *
import numpy as np
import seaborn as sns

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
Real_Table = Table.read_table('Data_Science/Data/Lotto_Sampling0.csv')
Real_win = Real_Table.column(1)
Real_Table = ""

for i in range(10):
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
var = np.var(win_cnt_list)
print("Avg of all data: " + avg)
print("Variance of all data: " + var)

win_table = Table().with_column('Win_cnt', win_cnt_list)
win_table.hist(bins = np.arange(0, 30, 1))

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

all_data = [Sample_list0, Sample_list1, Sample_list2, Sample_list3, Sample_list4, Sample_list5, Sample_list6, Sample_list7, Sample_list8, Sample_list9, Sample_list10]
ax = sns.boxplot(data = all_data, width = 0.5)
for i in range(11):
    sns.stripplot(x = [i], y = Real_win[i], color = 'red', jitter = True, size = 5)
ax.set_xticklabels(['18', '118', '218', '318', '418', '518', '618', '718', '818', '918', '1018'])
ax.set_xlabel('Index')
ax.set_ylabel('Values')
plots.title('Boxplot of Samples')
plots.ylabel('Win_cnt')
plots.show()



