import math
d = input("Введіть радіус клумби: ")
ogor = int(d) * math.pi * 2
sad = (int(d) ** 2 * math.pi)*4
print("Потрібно закупити: " + str(int(ogor)) + " метрів огорожі та " + str(int(sad)) + " штук саджанців.")