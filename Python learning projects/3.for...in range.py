# -*- coding: iso-8859-1 -*-
#queremos criar copões com a função for
#temos a marca; ano; promoção; amount (quantidade de cupões)

marca=str(input("Insira a marca: "))
ano=int(input("Insira o ano: "))
promocao=int(input("Qual o valor da promoção?"))
amount=int(input("Quantos cupões?"))
for num in range(amount):
    print(f"cupão {marca}/{ano}/{promocao}/{num}")
    print(f"{amount} cupões criados")
