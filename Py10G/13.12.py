#------------------------------------------------------------------------  
print("Завдання 1")
g = "так"
while g == "так":
    a = int(input("Введіть скільки сторін у фугури(3-6): "))
    if a == 3:
        print("Трикутник")
    elif a == 4:
        print("Чотирикутник")
    elif a == 5:
        print("П'ятикутник")
    elif a == 6:
        print("Шестикутник")
    else:
        print("Ви ввели не ту кількість сторін")
    g = input("Бажаєте певторити? ")
#------------------------------------------------------------------------  
print("Завдання 2")
a = []
for i in range(1, 10):
    a.append(i)
for i in range(len(a)):
    if a[i] == 1:
        print("1st")
    elif a[i] == 2:
        print("2nd")
    elif a[i] == 3:
        print("3rd")
    else:
        print(f"{a[i]}th", end="\n")
#------------------------------------------------------------------------  
print("Завдання 3")
g = "так"
while g == "так":
    a = int(input("Введіть число: "))
    if a%2 == 0:
        print("Парне")
    else:
        print("Непарне")
    g = input("Бажаєте певторити? ")
#------------------------------------------------------------------------  
print("Завдання 4")
g = "так"
while g == "так":
    a = int(input("Введіть рік: "))
    if a%4 == 0 and a%100 != 0 or a%400 == 0:
        print("Leap year")
    else:
        print("Ordinary")
    g = input("Бажаєте певторити? ")
#------------------------------------------------------------------------  
print("Завдання 5")
g = "так"
while g == "так":
    n = input("Ввдіть назву клітинки: ")
    i = 1
    while i < 9:
        if i%2 != 0:
            if n == "A"+str(i) or n == "B"+str(i+1) or n == "C"+str(i) or n == "D"+str(i+1) or n == "E"+str(i) or n == "F"+str(i+1) or n == "G"+str(i) or n == "H"+str(i+1):
                print("BLACK")
                break
            elif n == "B"+str(1) or n == "D"+str(1) or n == "F"+str(1) or n == "H"+str(1):
                print("WHITE") 
                break
        else:
            if n == "A"+str(i) or n == "B"+str(i+1) or n == "C"+str(i) or n == "D"+str(i+1) or n == "E"+str(i) or n == "F"+str(i+1) or n == "G"+str(i) or n == "H"+str(i+1):
                print("WHITE")  
        i += 1
    g = input("Бажаєте певторити? ")
#------------------------------------------------------------------------  
print("Завдання 6")
g = "так"
while g == "так":
    a = input("Введіть слово: ")
    b = []
    for i in a:
        b.append(i)
    i = len(b)-1
    c = []
    while i != -1:
        c.append(b[i])
        i -= 1
    if "".join(b) == "".join(c):
        print("is a palindrome")
    else:
        print("is not a palindrome")
    g = input("Бажаєте певторити? ")
#------------------------------------------------------------------------  
print("Завдання 7")
a = int(input("Введіть кількість рядків: "))
b = int(input("Введіть кфлькість стовпців: "))
for i in range(1,a+1):
    for a in range(1,b+1):
        print(f"{a} * {i} = {i*a}", end=" ")
    print("\n")
#------------------------------------------------------------------------  
print("Завдання 8")
a = int(input("Введіть число: "))
b = []
while a != 0:
    if a%2 == 1:
        b += "1"
        a = a//2
    else:
        b += "0"
        a = a/2
b = list(reversed(b))
for i in b:
    print(i, end="")
a = input("\nБажаєшь спробувати навпаки? ")
while a == "так":
    x = int(input("Введіть ка число: "),2)
    print(x)
    a = input("Бажаєшь ще спробувати? ")
#------------------------------------------------------------------------  
print("Завдання 9")
a = input("Введіть що бажаєте зашифрувати: ")
a = a.upper()
b = []
for i in a:
    b.append(i)
m = []
for i in range(len(b)):
    m.append(ord(b[i])+3)
c = []
for i in range(len(m)):
    if chr(m[i]-3) == "X":
        c.append(chr(65))
    elif chr(m[i]-3) == "Y":
        c.append(chr(66))
    elif chr(m[i]-3) == "Z":
        c.append(chr(67))
    else:
        c.append(chr(m[i]))
print("".join(c))