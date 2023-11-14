from datascience import *
import numpy as np

import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

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

for i in range(2):
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
