# test1 is about floating-point.
import sys
a = 0.01
formatted_a = "{:.55f}".format(a)
print(a, formatted_a)
result = 0.0
for i in range(100):
    result += a
print(a, result)

b = 0.3
formatted_b = "{:.55f}".format(b)
print(0.1 + 0.2, formatted_b)
print((0.1+0.2) == 0.3)

print(round(0.1 + 0.2, 5) == round(0.3, 5))

# Finding python's epsillon
print(sys.float_info)

max = sys.float_info.max
min = sys.float_info.min
print(min)
print(max, "\n")

# If num is 1
num = 1
ep = 1
while True:
    if ep + num <= num:
        break
    ep = ep / 2

print("EP Below = ", ep)

m = 1 + ep
print("1 + EP Below = ", m)

ep = 2 * ep
print("EP = ", ep)

m = 1 + ep
print("1 + EP = ", m, "\n")

# If num is 10000
num = 10000
ep = 1
while True:
    if ep + num <= num:
        break
    ep = ep / 2

print("EP Below = ", ep)

m = 1 + ep
print("1 + EP Below = ", m)

ep = 2 * ep
print("EP = ", ep)

m = 1 + ep
print("1 + EP = ", m, "\n")
