# -*- coding: iso-8859-1 -*-
number=[1,5,8,11]
acao=str(input("Que ação deseja tomar? append, insert ou pop? "))
if acao=="append":
    num_add_fim=int(input("Qual número deseja adicionar no fim? "))
    number.append(num_add_fim)
elif acao=="insert":
    index=int(input("Indique o índice: "))
    num_add_index=int(input(f"Qual numero que deseja adicionar no índice {index}?"))
    number.insert(index,num_add_index)
elif acao=="pop":
    index=int(input("Indique o índice: "))
    remove=number.pop(index)
else:
    print("Insire uma ação válida")
print(number)
