import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-whitegrid')
import numpy as np

x = np.linspace(0, 10, 1000)

plt.plot(x, np.sin(x))
plt.xlim(-1, 11)
plt.ylim(-1.5, 1.5)
plt.show()

plt.plot(x, np.sin(x))
plt.xlim(10, 0)
plt.ylim(1.2, -1.2)
plt.show()

plt.plot(x, np.sin(x))
plt.axis([-1, 11, -1.5, 1.5])
plt.show()

plt.plot(x, np.sin(x))
plt.axis('tight')
plt.show()

plt.plot(x, np.sin(x))
plt.axis('equal')
plt.show()

plt.plot(x, np.sin(x))
plt.title("A Sine Curve")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.show()

plt.plot(x, np.sin(x), '-g', label = 'sin(x)')
plt.plot(x, np.cos(x), ':b', label = 'cos(x)')
plt.axis('equal')
plt.legend()
plt.show()
