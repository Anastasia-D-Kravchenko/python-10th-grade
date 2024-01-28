print("Задача 1.")
a=float(input("Введіть число a:"))
b=float(input("Введіть число b:"))
sum = round((a + b), 2)
min = round((a - b), 2)
mno = round((a * b), 2)
deli = round((a / b), 2)
deli1 = round((b/a), 2)
print("Їх сума: "+str(sum)+" . Їх різниця: "+str(min)+". Їх добуток: "+str(mno)+" . Їх частка: "+str(deli)+" і "+str(float(deli1)))
print("Задача 2.")
ch=float(input("Введіть число:"))
ch = round(ch,3)
ch = abs(ch)
print("Ваше число: "+str(ch))
print("Задача 3.")
ser=4
ser1=ser*3
ser2=(-ser)*3
ser3=ser**ser**ser
ser4=ser/ser/ser
ser0 = max(ser1,ser2,ser3,ser4)
print("Ваше число: "+str(ser0))
print("Задача 4.")
st = "Чемпіонат України з футболу"
x = "Чемпіонат України"
if x in st:
    print(f"Так, ці слова: '{x}' присутні у реченні: {st}")
print("Задача 5.")
zm = "зменшення значення "
zp = "змінної"
zm += zp
print(zm)
print("Задача 6.")
zile = int(input("Введіть число:"))
ost = zile%10
per = zile//10
zile = str(ost)+str(per)
print(zile)
print("Задача 6.1")
zile_ny = int(input("Введіть число:"))
zi = zile_ny//1000
zi1 = zile_ny//100%10
le = zile_ny//10%10
le1 = zile_ny%10
zile_ny = str(le1)+str(le)+str(zi1)+str(zi)
print(zile_ny)
print("Задача 6.2")
zile_n = int(input("Введіть число:"))
zi11 = zile_n//100%10
le1 = zile_n//10%10
le11 = zile_n%10
zile_n = str(le11)+str(le1)+str(zi11)
print(zile_n)
print("Задача 8.")
zile = int(input("Введіть число:"))
ost = zile%10
per = zile//10
zile = str(per)*2+str(ost)*2
print(zile)
print("Задача 9.")
Dryzi_sym = input("Введіть на яку суму друзі в кафе отримали рахунок:")
Dryzi_sym = int(Dryzi_sym)
Off = (Dryzi_sym * 10) / 100
Dryzi_sym = Dryzi_sym + Off
Koshen = Dryzi_sym/3
print("Кожен з друзів повинен заплатити по: " + str(int(Koshen)))
print("Задача 10.")
vid = 4500
wv = 70*1.6
god = vid/wv
print("Ви прибудете через: " + str(int(round(god,0)))+" годин.")
print("Задача 11.")
vid = 4500
podor = 20
gal = 3.78
var = 0.75
st_ben = gal*var
st_vut = (vid*1.6)/20
st_pod = st_vut*st_ben
print("Вартість 1 галону бензину: " + str(st_ben) + " . Витрачено бензину на подорож: " + str(int(st_vut)) + " . Вартість бензину, що витрачено на подорож: " + str(st_pod))
print("Задача 12.")
do = 13
posl = 45
posl = posl + 10 + 30 + 20
otdux = posl - 45
while otdux >= 60:
    otdux -= 60
    otdux += 1
do1 = 15
posl1 = 30
posl1 = 15 + (2*60 + 10) + 2*60 
while posl1 > 60:
    do1+=1
    posl1 -= 60
print("Боб провів в приміщенні аеропорту Калгарі: " + str(otdux) + " годин. Він прибуде у Вінніпег за місцевим часом о: " + str(do1)+":"+str(posl1))
otdux = posl - 45 + 45 +15
while otdux >= 60:
    otdux -= 60
    otdux += 1
print("Якщо Боб ще 45 хв до виліту літака та 15 поки той стояв був у аеропорту, тоді: "+str(otdux)+" години")