# #------------------------------------------------------------------------  
# print("Завдання 1")
# a = [12, "HI", True]
# b = [3, 4, "BYE", False]
# print(a,b)
# #------------------------------------------------------------------------  
# print("Завдання 2")
# a.pop(1) # a.remove("HI")
# #------------------------------------------------------------------------  
# print("Завдання 3")
# print(a)
# #------------------------------------------------------------------------  
# print("Завдання 4")
# b.pop(len(b)-1)
# #------------------------------------------------------------------------  
# print("Завдання 5")
# print(b)
# #------------------------------------------------------------------------  
# print("Завдання 6")
# a.extend(b)
# #------------------------------------------------------------------------  
# print("Завдання 7")
# print(a)
# #------------------------------------------------------------------------  
# print("Завдання 8")
# c = a[1:4]
# #------------------------------------------------------------------------  
# print("Завдання 9")
# print(c)
# #------------------------------------------------------------------------  
# print("Завдання 10")
# c.insert(0,"I'M FIRST")
# c.append("I'M LAST")
# print(c)
#------------------------------------------------------------------------  
print("Завдання 1")
a = [12, 20, 3, 8, 33, 1]
b = 0
for x in a:
    if x > 8:
        print(x*3, end=" ")
        b += x*3
print("\nСума чисел:",b)
#------------------------------------------------------------------------  
print("Завдання 2")
a = [13, 19, 11, 7, 18]
a.pop(0)
print(max(a))
#------------------------------------------------------------------------  
print("Завдання 3")
a = ["Херсон", "Житомир", "Ужгород", "Харків"]
a.insert(1,"Луцьк")
a.sort()
print(a)
#------------------------------------------------------------------------  
print("Завдання 4")
a = [9, 2, 5, 6]
a[0]=12
a.sort()
print(a)
#------------------------------------------------------------------------  
print("Завдання 5")
a = [51, 3, 16, 82, 37, 8]
b = max(a)
a.pop(1)
a.sort()
a.insert(3,5)
a.insert(0,10)
print(a)
#------------------------------------------------------------------------  
print("Завдання 6")
a = ["Python" , 1991 ]
b = ["Гвидо ван"]
print(f"Мову {a[0]} розробив у {a[1]} році {b[0]} Россум.")