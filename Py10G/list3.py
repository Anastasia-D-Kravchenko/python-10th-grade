from random import randint
#------------------------------------------------------------------------  
print("Завдання 1")
a = []
for i in range(10):
    a.append(randint(0, 5))
print(a)
c = []
i = 0
while i != len(a):
    if a[i] == max(a):
        c.append(i)
    i += 1
print(c)
#------------------------------------------------------------------------  
print("Завдання 2")
a = []
for i in range(10):
    a.append(randint(0, 5))
print(a)
i = len(a)-1
c = []
while i >= 0:
    c.append(a[i])
    i -= 1
print(c)
#------------------------------------------------------------------------  
print("Завдання 3")
a = []
for i in range(10):
    a.append(randint(0, 5))
print(a)
i = 0
c = []
c.extend(a)
c[0] = c[len(c)-1]
c.pop(len(c)-1)
c.append(a[1])
c[1] = c[len(c)-2]
c.pop(len(c)-2)
c.append(a[0])
print(c)
#------------------------------------------------------------------------  
print("Завдання 4")
a = []
b = []
for i in range(10):
    a.append(randint(0, 10))
    b.append(randint(0, 10))
print(a)
print(b)
c = []
i = 0
while i != len(a):
    if i%2 == 0:
        c.append(a[i])
        c.append(b[i])
    else:
        c.append(b[i])
        c.append(a[i])
    i += 1
print(c)
#------------------------------------------------------------------------  
print("Завдання 5")
a = input("Введіть назву карти: ")
b = list(a)
if b[0]+b[1] == "34" or b[0]+b[1] == "37":
    if len(b) == 15:
        print("American Express")
    else:
        print("No")
elif b[0]+b[1] == "51" or b[0]+b[1] == "52" or b[0]+b[1] == "53" or b[0]+b[1] == "54" or b[0]+b[1] == "55":
    if len(b) == 16:
        print("MasterCard")
    else:
        print("No")
elif b[0] == "4":
    if len(b) == 16 or len(b) == 13:
        print("Visa")
    else:
        print("No")
elif b[0]+b[1] == "50" or b[0]+b[1] == "58" or b[0]+b[1] == "63" or b[0]+b[1] == "67" or b[0]+b[1] == "06":
    if len(b) == 12 or len(b) == 13 or len(b) == 14 or len(b) == 15 or len(b) == 16 or len(b) == 17 or len(b) == 18 or len(b) == 19:
        print("Maestro")
    else:
        print("No")
else:
    print("No")