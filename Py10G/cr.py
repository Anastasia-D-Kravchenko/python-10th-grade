import random
#------------------------------------------------------------------------  
print("Завдання 1")
a = int(input("Введіть число: "))
for i in range(1,11):
    print(f"{a} * {i} = {i*a}")
#------------------------------------------------------------------------  
print("Завдання 2")
a = 1.75
for i in range(1,10):
    print(f"{i} порцій коштують {a*i} грн")
#------------------------------------------------------------------------  
print("Завдання 3")
for a in range(1,10):
    for b in range(1,10):
        if a != b:
            print(f"{a}{b}", end=" ")
#------------------------------------------------------------------------  
print("\nЗавдання 4")
b = 0
for i in range(15):
    a = random.randint(-10, 10)
    b += a
    print(a, end=" ")
print("\nСума ціх чисел:",b)
#------------------------------------------------------------------------  
print("Завдання 5")
b = 0
for i in range(1, 11):
    a = random.randint(-15, 15)
    print(f"Число {i} = {a}")
    if a < 0:
        b += 1
print(f"Від'ємних чисел: {b}")