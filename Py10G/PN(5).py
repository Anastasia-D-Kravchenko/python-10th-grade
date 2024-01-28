#«Кімната»
print("«Кімната»")
x = input("Введите довжину кімнати:")
y = input("Введите ширину кімнати:")
per = 2 * (int(x) + int(y))
plo = int(x) * int(y)
print("Периметр: " + str(per) + " Площа: " + str(plo))
#«Учень»
print("«Учень»")
Levko_x = input("Введить скільки хвилин Левко чухав потилицю і дивився у вікно:")
Levko_y = input("Введить скільки хвилин він шукав гумку:")
Levko_z = input("Введіть скільки хвилин він малював карекатуру свого товариша:")
Levko = (120 - int(Levko_x) - int(Levko_y) - int(Levko_z)) / 5
print("Левко переклав: " + str(Levko))
#«Дівчатка»
print("«Дівчатка»")
Daruna = input("Введіть скільки важить Дарина:")
Natalia = int(Daruna) + 5
Tcykor = input("Введіть скільки вижить цукор(рукомендую більше ніж: "+str(Natalia+Natalia-5)+"):")
Treba = int(Tcykor) - (Natalia + (Natalia - 5))
print("Дівчатам потрібно з'їсти: " + str(Treba) + " кг")
#«Куб»
print("«Куб»")
Kyb = input("Введите довжину ребра куба:")
Kyb = int(Kyb)
Pl = Kyb ** 2
Po = Pl * 6
Ob = Kyb ** 3
print("Об'єм куба: " + str(Ob) + ". Площа всієї поверхні куба: " + str(Po))
#«Зарплата»
print("«Зарплата»")
Zar = input("Введите закобітню плату працівника:")
Zar = int(Zar)
Podatku = (Zar * 186) / 1000
Ost = Zar - Podatku
Soct = (Zar * 22) / 100
Sym = Podatku + Soct
print("Виплачено заробітню плату в розмірі: " + str(int(Ost)) + ". Суму податків становить: " + str(int(Sym)))
#«Кафе»
print("«Кафе»")
Dryzi_sym = input("Введіть на яку суму друзі в кафе отримали рахунок:")
Dryzi_sym = int(Dryzi_sym)
Off = (Dryzi_sym * 10) / 100
Dryzi_sym = Dryzi_sym + Off
Koshen = Dryzi_sym/3
print("Кожен з друзів повинен заплатити по: " + str(int(Koshen)))
#«Пінгвіни»
print("«Пінгвіни»")
N = input("Введіть число від 1-9: ")
N = int(N)
tab = "\t"
head = (" "+" _~_\t")*N
eye = " (o o)\t"*N
hends = " / V \ \t"*N
body = "/( _ )\ "*N
leg = " ^^ ^^ \t"*N
if(N > 9):
        print("Ви ввели неправильне число")
else:
        print(str(head)+"\n"+str(eye)+"\n"+str(hends)+"\n"+str(body)+"\n"+str(leg))
