# -*- coding: iso-8859-1 -*-
nomes=["Pedro","Jo�o","Filipe","Ant�nio","Bruno","Manuel","Nuno","Joaquim","Lu�s","Diogo"]
#indexing
nomes1=nomes[0:5]#nomes do primeiro at� ao quarto nome
nomes2=nomes[2:7]#nomes do terceiro at� ao sexto
nomes3=nomes[1::2]#nomes do segundo at� ao �ltimo com saltos de 2
print(nomes1)
print(nomes2)
print(nomes3)

#negative indexing
nomes4=nomes[-2]#pen�ltimo nome
nomes5=nomes[-1]#�ltimo nome
nomes6=nomes[::-1]#nomes todos na ordem contr�ria
nomes7=nomes[::-2]#nomes na ordem contr�ria com saltos de dois
nomes8=nomes[-1:0:-1]#nomes na ordem contr�ria a come�ar no �ltimo e terminar no segundo
print(nomes4)
print(nomes5)
print(nomes6)
print(nomes7)
print(nomes8)
