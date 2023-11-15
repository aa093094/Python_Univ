def func_f(x,y):
  ff= y - x - 2*(x**2) - 2*(x*y) - y**2
  return ff

import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.use('TkAgg')

#### 랜덤 서치
maxN = 100001
maxf = -10000
for i in range(maxN):
  x = -2 + 4 * np.random.random_sample()
  y = 1 + 2 * np.random.random_sample()
  fn = func_f(x, y)
  if fn > maxf :
    maxf = fn
    maxx = x
    maxy = y
  #if i == 1000 or i==2000 or i==3000 or i==4000:
  if (i % 5000) == 0 :
    print("i:{}, x{}, y{}, maxf:{}" .format(i, maxx, maxy, maxf))


#### End of 랜덤 서치

maxN = 101
maxf = -1000
x = -2
y = 1
for j in range(100):
  for i in range(maxN):
    x = -2 + 4 * np.random.random_sample()
    fn = func_f(x, y)
    if fn > maxf :
      maxf = fn
      maxx = x
    if (i % 100) == 0 :
      print("j{}, i:{}, x:{}, y:{}, maxf:{}" .format(j, i, maxx, maxy, maxf))

  for i in range(maxN):
    y = 1 + 2 * np.random.random_sample()
    fn = func_f(x, y)
    if fn > maxf :
      maxf = fn
      maxy = y
    if (i % 100) == 0 :
      print("j{}, i:{}, x:{}, y:{}, maxf:{}" .format(j, i, maxx, maxy, maxf))

print("x:{}, y:{}, maxf:{}" .format(maxx, maxy, maxf))

n = 100
xmin, xmax, ymin, ymax, zmin, zmax = 0, 20, 0, 20, 0, 50
cmin, cmax = 0, 2

xs = np.array([(xmax - xmin) * np.random.random_sample() + xmin for i in range(n)])
ys = np.array([(ymax - ymin) * np.random.random_sample() + ymin for i in range(n)])
zs = np.array([(zmax - zmin) * np.random.random_sample() + zmin for i in range(n)])
color = np.array([(cmax - cmin) * np.random.random_sample() + cmin for i in range(n)])

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(xs, ys, zs, c=color, marker='o', s=30, cmap='Greens')

plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-3, 3, 11)
X = np.tile(x, (11, 1))
Y = np.transpose(X)
Z = func_f(X, Y)                    # !!!

ax.plot_surface(X, Y, Z)
ax.set_zlim(-10, 10)

plt.tight_layout()
plt.show()




