lista = [7,5,8,90,10,10,10]
listb = [10,7,0,7]
sumlist = []

lista.reverse()
listb.reverse()

a = 0
###while a < len(lista):
#    c = lista[a] + listb[a]
 #   sumlist.append(c)
  #  a += 1

for i in lista:
    c = lista[a] + listb[a]
    sumlist.append(c)
    a += 1

sumlist.reverse()
print(sumlist)