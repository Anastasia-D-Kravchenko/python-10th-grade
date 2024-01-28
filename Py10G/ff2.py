gr = int(input("Введіть скільки у Петрика грошей:"))
pur = int(input("Введіть скільки стоють пиріжки:"))
ost_p = gr/pur
ost_g = gr - (pur*int(ost_p))
print("Петрик купить: "+str(int(ost_p))+" штук пиріжків. У нього залишиться: "+str(ost_g)+" грн.")