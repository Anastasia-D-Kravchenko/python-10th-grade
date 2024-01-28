a = [45, 23.5, 76, 29, 41]
b = min(a)
c = max(a)
print(b, ",", c)

x = [5, 7, 8, 12, 4]
f = 0
for i in range(len(x)):
    if x[i] > 5:
        f += x[i]
x = f
print(x)

m = [17, 44, 5, 21, 22, 38, 9]
m.remove(max(m))
m.insert(2, 19)
m.sort()
print(m)