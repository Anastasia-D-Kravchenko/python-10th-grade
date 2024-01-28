# #------------------------------------------------------------------------  
# print("Завдання 1(з підручника)")
# a = [['команда', 'файл', 'біт'],['смартфон','миша','байт']]
# print(a[0][1],a[1][2])
# #------------------------------------------------------------------------  
# print("Завдання 2(з підручника)")
# a = [[5, 3, 12], [13, 7, 7], [21, 6, 8]]
# i=0
# b=0
# c=0
# while i != len(a):
#     while b != (len(a[i])):
#         c += a[i][b]
#         b += 1
#     b = 0
#     i += 1
# print(c)
# #------------------------------------------------------------------------  
# print("Шпора")
# n = int(input())
# a = []
# for i in range(n):
#     b = input().split()
#     for i in range(len(b)):
#         b[i] = int(b[i])
#     a.append(b)
# print(a)
#------------------------------------------------------------------------  
print("Завдання 1")
n = int(input())
a = []
c = 0
for i in range(n):
    b = input().split()
    for i in range(len(b)):
        b[i] = int(b[i])
        if b[i] > 0:
            if b[i]%2 != 0:
                c += b[i]
    a.append(b)
print(f"Суму всіх додатних непарних елементів {a} становить: {c}")
#------------------------------------------------------------------------  
print("Завдання 2")
n = int(input())
a = []
c = 0
for i in range(n):
    b = input().split()
    for i in range(len(b)):
        b[i] = int(b[i])
        if b[i] > 0:
            if b[i]%2 == 0:
                c += b[i]
    a.append(b)
print(f"Суму всіх додатних парних елементів {a} становить: {c}")
#------------------------------------------------------------------------  
print("Завдання 3")
n = int(input())
a = []
c = 0
for i in range(n):
    b = input().split()
    for i in range(len(b)):
        b[i] = int(b[i])
        if b[i] > c:
            c = b[i]
    a.append(b)
print(f"Найбільший елемент цього масиву: {c}")
#------------------------------------------------------------------------  
print("Завдання 4")
n = int(input())
a = []
for i in range(n):
    b = input().split()
    for i in range(len(b)):
        b[i] = int(b[i])
    a.append(b)
q = []
h = []
for i in range(len(a)):
    for j in range(n):
        q.append(a[j][i])
    h = min(q)
print(f"Найменший елемент цього масиву: {h}")
#------------------------------------------------------------------------  
print("Завдання 5")
n = int(input())
a = []
for i in range(n):
    b = input().split()
    for i in range(len(b)):
        b[i] = int(b[i])
    a.append(b)
c = 0
q = []
for i in range(n):
    q.append(max(a[i]))
print(f"Найбільший елемент рядка: {q}")
#------------------------------------------------------------------------  
print("Завдання 6")
n = int(input())
a = []
for i in range(n):
    b = input().split()
    for i in range(len(b)):
        b[i] = int(b[i])
    a.append(b)
c = 0
q = []
for i in range(n):
    q.append(min(a[i]))
print(f"Найменший елемент рядка: {q}")
#------------------------------------------------------------------------  
print("Завдання 7")
n = int(input())
a = []
for i in range(n):
    b = input().split()
    for i in range(len(b)):
        b[i] = int(b[i])
    a.append(b)
q = []
h = []
for i in range(len(a)):
    for j in range(n):
        q.append(a[j][i])
    h.append(max(q))
    q.clear()
print(f"Найбільший елемент стовпця: {h}")
#------------------------------------------------------------------------  
print("Завдання 8")
n = int(input())
a = []
for i in range(n):
    b = input().split()
    for i in range(len(b)):
        b[i] = int(b[i])
    a.append(b)
q = []
h = []
for i in range(len(a)):
    for j in range(n):
        q.append(a[j][i])
    h.append(min(q))
    q.clear()
print(f"Найменший елемент стовпця: {h}")