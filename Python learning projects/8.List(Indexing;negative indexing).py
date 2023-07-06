# -*- coding: iso-8859-1 -*-
nomes=["Pedro","João","Filipe","António","Bruno","Manuel","Nuno","Joaquim","Luís","Diogo"]
#indexing
nomes1=nomes[0:5]#nomes do primeiro até ao quarto nome
nomes2=nomes[2:7]#nomes do terceiro até ao sexto
nomes3=nomes[1::2]#nomes do segundo até ao último com saltos de 2
print(nomes1)
print(nomes2)
print(nomes3)

#negative indexing
nomes4=nomes[-2]#penúltimo nome
nomes5=nomes[-1]#último nome
nomes6=nomes[::-1]#nomes todos na ordem contrária
nomes7=nomes[::-2]#nomes na ordem contrária com saltos de dois
nomes8=nomes[-1:0:-1]#nomes na ordem contrária a começar no último e terminar no segundo
print(nomes4)
print(nomes5)
print(nomes6)
print(nomes7)
print(nomes8)
