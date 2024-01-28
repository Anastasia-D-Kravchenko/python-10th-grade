from random import *
#------------------------------------------------------------------------  
print("Завдання 1")
a = []
for i in range(10):
    a.append(randint(0, 30))
print(a)
print(max(a))
#------------------------------------------------------------------------  
print("Завдання 2")
a = []
for i in range(10):
    a.append(randint(-30, 30))
print(a)
ma = max(a)
mi = min(a)
riz = abs(ma - mi)
print(f"Різниця між {ma} - {mi} =", riz)
#------------------------------------------------------------------------  
print("Завдання 3")
a = []
for i in range(10):
    a.append(randint(-30, 30))
print(a)
ma = max(a)
mi = min(a)
i = 0
c = []
while i != len(a):
    if ma == a[i]:
        c.append(i)
    elif mi == a[i]:
        c.append(i)
    i += 1
c1 = abs((c[0]+1)-c[1])
print(f"Знаходяться на {c[0]} та {c[1]}:",c1)
#------------------------------------------------------------------------  
print("Завдання 4")
a = []
for i in range(10):
    a.append(randint(0, 30))
print(a)
ma = max(a)
mi = min(a)
i = 0
c = []
while i != len(a):
    if ma == a[i]:
        c.append(mi)
    elif mi == a[i]:
        c.append(ma)
    else:
        c.append(a[i])
    i += 1
print(c)
#------------------------------------------------------------------------  
print("Завдання 5")
a = []
for i in range(10):
    a.append(randint(0, 30))
print(a)
i = 0
c = []
while i != len(a):
    if a[i]%2 == 0:
        c.append(a[i])
    i += 1
c = max(c)
print(c)
#------------------------------------------------------------------------  
print("Завдання 6")
a = []
for i in range(10):
    a.append(randint(-30, 30))
print(a)
i = 0
c = []
while i != len(a):
    if a[i] > 0:
        c.append(a[i])
    i += 1
c = min(c)
print(c)
#------------------------------------------------------------------------  
print("Завдання 7")
na = '4929373040107907'
na = list(map(int, na))
suma = 0
for id, znch in enumerate(na):
    if id%2 != 0:#Якщо 0 вважати нейтральним
        suma += znch
    else:
        c = znch * 2
        if c/2 >= 5:
            c = c%10 + c//10
        suma += c
if suma%10 == 0:
    print("yes")
else:
    print("no")