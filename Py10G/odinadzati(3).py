import random #Я подивилась там рандом 100 включати буде, тому виправлена версія:
#------------------------------------------------------------------------  
print("Завдання 1")
a = int(input("Введіть число: "))
while a != 0:
    a = int(input("Введіть число: "))
#------------------------------------------------------------------------  
print("Завдання 2")
a = random.randint(1,7)
while a != 1:
    print(a)
    a = random.randint(1,7)
#------------------------------------------------------------------------  
print("Завдання 3")
a = random.randint(1,100)
b = 0
while a != 100:
    b += 1
    print(a, end=" ")
    a = random.randint(1,100)
print("\nУсього:",b)
#------------------------------------------------------------------------  
print("Завдання 4")
a = random.randint(1,100)
b = 0
c = 0
while a != 100:
    a = random.randint(1,100)
    if a%2 != 0:
        c += 1
        print(a, end=" ")
    else:
        b += 1
print(f"\nПарних чисел {b}, а непарних {c}(в горі виведені непарні)")
#------------------------------------------------------------------------  
print("Завдання 5")
a = random.randint(1,100)
b = 0
c = 0
b1 = 0
c1 = 0
while a != 100:
    if a%2 != 0:
        c += 1
        c1 += a
        print(a, end=" ")
    else:
        b += 1
        b1 += a
        print(a, end=" ")
    a = random.randint(1,100)
if b != 0 and c != 0:
    b1 = b1/b
    c1 = c1/c
    print(f"\nПарних чисел {b}, а непарних {c}.\nСередне арифметичне {b1}, {c1}")
else:
    print("Ось це у вас вдача, прям як в мене, перше ж число і 100, а на 0 делити не можна")
#------------------------------------------------------------------------  
print("Завдання 6")
a = random.randint(1,10)
b = int(input("Спробуеш? "))
c = 1
while a != b:
    print("Ні мимо.")
    b = int(input("Спробуеш? "))
    c += 1
print(f"Так вірно! В нас мендальний зв'язок;)\nЦе в тебе зайняло аж {c} спроб")
#------------------------------------------------------------------------  
print("Завдання 7?")
print("1- не парне. 2- парне")
a = int(input("Ну що давай подивимося, вводи число: "))
while a != 1:
    if a != 0:
        if a%2 == 0:
            a /= 2
            print(a, end=" (2) ")
        else:
            a = a*3+1
            print(a, end=" (1) ")
    else:
        print("Що не очікували? А я спробувала. Чуть не задимівся комп'ютер:)До речі 0 виняток з правил, бо 1 він ніколи не дасть.(Хоча 0^0=1;0!=1 Про факторіал сама не знала, гугл корисна річь)")
        break
if a == 1:
    print(f"\nТак усі числа при цьому в результаті дадуть {int(a)}")
else:
    print("Видають нобілевські премії за такою адресою: ")