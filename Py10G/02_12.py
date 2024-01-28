#------------------------------------------------------------------------  
print("Завдання 1.1")
test1 = 'Test variable to write to file'
file = open('tests.txt', 'wt')
text = file.write(test1)
print(text)
file.close()
#------------------------------------------------------------------------  
print("Завдання 1.2")
file = open('tests.txt', 'rt')
test2 = file.read()
file.close()
print(test2)
#------------------------------------------------------------------------  
print("Завдання 1.3")
if test1 == test2:
    print("Нічого собі вони ідентичні!")
else:
    print("Це що таке? Ми не на це домовлялися.")
#------------------------------------------------------------------------  
print("Завдання 2.1")
from random import *
new = open('numbers.txt', 'wt')
for i in range(1,11):
    a = randint(1,100)
    print(a, file=new, sep='')
file.close()
new = open('numbers.txt', 'rt')
a = new.readlines()
b = 0
for i in range(len(a)):
    b += int(a[i])
print(b)
sum = open('sum_numbers.txt', 'wt')
print(b, file=sum)
file.close()
#------------------------------------------------------------------------  
print("Завдання 2.2")
a = int(input("Введіть число: "))
b = open('parno.txt', 'wt')
if a%2 == 0:
    b.write(f'{a} - double')
else:
    b.write(f'{a} - unpaired')
file.close()