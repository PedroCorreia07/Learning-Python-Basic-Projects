# -*- coding: iso-8859-1 -*-
#queremos criar cop�es com a fun��o for
#temos a marca; ano; promo��o; amount (quantidade de cup�es)

marca=str(input("Insira a marca: "))
ano=int(input("Insira o ano: "))
promocao=int(input("Qual o valor da promo��o?"))
amount=int(input("Quantos cup�es?"))
for num in range(amount):
    print(f"cup�o {marca}/{ano}/{promocao}/{num}")
    print(f"{amount} cup�es criados")
