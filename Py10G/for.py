import random
#------------------------------------------------------------------------  
print("Завдання 1")
for i in range(1,11):
    print(f"2 * {i} = {i*2}")
#------------------------------------------------------------------------  
print("Завдання 2")
for i in range(1,11):
    print(f'---{i}---')
    for a in range(1,11):
        print(f"{a} * {i} = {i*a}")
#------------------------------------------------------------------------  
print("Завдання 3")
for i in range(-10,11):
    a = 4*(i)**2+3*i+2
    print(f"{4}*{(i)}^{2}+{3}*{i}+{2} = {a}")
#------------------------------------------------------------------------  
print("Завдання 4")
for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            if a != b and a != c and b != c:
                print(f"{a}, {b}, {c} = {a}{b}{c}")
#------------------------------------------------------------------------  
print("Завдання 5")
for i in range(0,10):
    a = random.randint(0, 10)
    print(a)
#------------------------------------------------------------------------  
print("Завдання 6")
b = 0
for i in range(0,10):
    a = random.randint(0, 20)
    b += a
print(b)
#------------------------------------------------------------------------  
print("Завдання 7")
b = 0
for i in range(1,16):
    a = random.randint(-5, 5)
    print(f"Число {i} = {a}")
    if a > 0:
        b += 1
print(f"Додатніх чисел: {b}")
#------------------------------------------------------------------------  
print("Завдання 8")
s = 0
for i in range(0,10):
    a = random.randint(1, 10)
    j = random.randint(1, 10)
    p = int(input(f"{a} * {j} = "))
    if p == (a*j):
        print(f"Так! {a} * {j} = {p}")
        s += 1
    else:
        print(f"Ні! {a} * {j} = {a*j}, а не {p}")
print(f"Ви знаєте {(s/10)*100}% таблички множення!")
if s > 8:
    print("Тримай кубок Переможця!")
else:
    print(f"Міг і краще!")