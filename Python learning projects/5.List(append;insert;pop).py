# -*- coding: iso-8859-1 -*-
number=[1,5,8,11]
acao=str(input("Que a��o deseja tomar? append, insert ou pop? "))
if acao=="append":
    num_add_fim=int(input("Qual n�mero deseja adicionar no fim? "))
    number.append(num_add_fim)
elif acao=="insert":
    index=int(input("Indique o �ndice: "))
    num_add_index=int(input(f"Qual numero que deseja adicionar no �ndice {index}?"))
    number.insert(index,num_add_index)
elif acao=="pop":
    index=int(input("Indique o �ndice: "))
    remove=number.pop(index)
else:
    print("Insire uma a��o v�lida")
print(number)
