from random import randint
mas = []
for i in range(10):
   mas.append(randint(-10, 10))
nozero = [a for a in mas if a > 0]
zero = [a for a in mas if a < 0]
print(sum(nozero))
print(len(nozero))
print(sum(nozero) / len(nozero))

print("\n")

print(sum(zero))
print(len(zero))
print(sum(zero) / len(zero))