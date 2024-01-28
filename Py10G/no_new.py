print("Завдання 1")
famous_person = "Konstantin Karikh once said, "
message = "'Do what you love freedom to love what you do happiness.'"
print(famous_person+message)
from cmath import pi
print("Завдання 2")
plosha = int(input("Введіть радіус круга: "))
plosha = plosha**2
plosha = plosha*pi
print("Площа круга становить: "+str(round(plosha, 2)))
import math
print("Завдання 3")
cat = int(input("Введіть катет: "))
gip = int(input("Введіть гіпотенузу: "))
teor = math.sqrt(pow(gip,2) - pow(cat,2))
print("Ваш катет: " + str(int(teor)))
print("Завдання 4")
sec = int(input("Введіть кількість секунд: "))
god = sec//3600
print("Стільки годин пройшло відпочатку вудліку: "+str(god))
print("Завдання 5")
sec = int(input("Введіть кількість секунд: "))
xv = sec%60
print("Стільки хвилин пройшло відпочатку вудліку: "+str(xv))
print("Завдання 6")
sec = int(input("Введіть кількість секунд: "))
god = sec//3600
c = (sec-god*3600)//60
print("Стільки хвилин пройшло відпочатку вудліку: "+str(c))
print("Завдання 7")
sec = int(input("Введіть кількість секунд: "))
god = sec//3600
c = sec%3600//60
xv = sec%60
print(str(god)+":"+str(c)+":"+str(xv))
print("Завдання 8")
time = int(input("Введіть скільки у вас зараз годин(тільки години): "))
time = time - 7 + 10 - 3 + 6
zag = 10 + 6
while time > 24:
    time -=24
print("Ви прибудете о Лос-Анжелес о: " + str(time)+" годині. Ваш загальний час подорожі: "+str(zag))
#Поправка 5 завдання з ср:
print("Поправка 5 завдання з ср:")
print("Задача 5")#Ось ця задача буда найскладніша в розумінні, але я впроралась, сподіваюсь) вона виведе всі цілі числа від а до б
a = float(input("Введіть число а: "))
b = float(input("Введіть число b: "))
g = int(abs(b-a))
print(f"Між числами {a}, {b} лежить ціле число: {g}")