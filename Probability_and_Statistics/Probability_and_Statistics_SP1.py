import matplotlib.pyplot as plt
import random
import numpy as np

List_x = []
sum = 0
List_y = []
Rand_nums = []

for i in range (1, 101):
    List_x.append(i)

for j in range (1, 101):
    num = random.randint(0, 1)
    Rand_nums.append(num)
    sum = sum + num
    List_y.append(sum/j)

data_10 = np.array(Rand_nums[0:10])
data_20 = np.array(Rand_nums[0:20])
data_30 = np.array(Rand_nums[0:30])
data_40 = np.array(Rand_nums[0:40])
data_50 = np.array(Rand_nums[0:50])
data_60 = np.array(Rand_nums[0:60])
data_70 = np.array(Rand_nums[0:70])
data_80 = np.array(Rand_nums[0:80])
data_90 = np.array(Rand_nums[0:90])
data_100 = np.array(Rand_nums[0:100])

print("Number of coin tosses\t      Var(Y)")
print("         10      \t" + str(np.var(data_10)/10))
print("         20      \t" + str(np.var(data_20)/20))
print("         30      \t" + str(np.var(data_30)/30))
print("         40      \t" + str(np.var(data_40)/40))
print("         50      \t" + str(np.var(data_50)/50))
print("         60      \t" + str(np.var(data_60)/60))
print("         70      \t" + str(np.var(data_70)/70))
print("         80      \t" + str(np.var(data_80)/80))
print("         90      \t" + str(np.var(data_90)/90))
print("         100      \t" + str(np.var(data_100)/100))

plt.plot(List_x, List_y)
plt.axis([0, 100, 0, 1])
plt.xlabel('Number of coin tosses')
plt.ylabel('Proportion of heads')
plt.grid(True)
plt.show()