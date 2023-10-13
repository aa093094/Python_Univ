from datascience import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
plt.style.use('fivethirtyeight')

united = Table.read_table('Data_Science/Data/united_summer2015.csv')
print(united, "\n")

print(united.column('Delay').min(), "\n", united.column('Delay').max(), "\n")

delay_bins = np.append(np.arange(-20, 301, 10), 600)
united.hist('Delay', bins = delay_bins, unit = 'minute')
plt.title("All datas of delays")
plt.show()

print(united.where('Delay', are.above(200)).num_rows/united.num_rows)

delay_bins = np.arange(-20, 201, 10)
united.hist('Delay', bins = delay_bins, unit = 'minute')
plt.title("Datas of -20 ~ 200 delays")
plt.show()

def empirical_hist_delay(n):
    united.sample(n).hist('Delay', bins = delay_bins, unit = 'minute')

empirical_hist_delay(10)
plt.title("Sampling 10 samples")
plt.show()

empirical_hist_delay(1000)
plt.title("Sampling 1000 samples")
plt.show()
