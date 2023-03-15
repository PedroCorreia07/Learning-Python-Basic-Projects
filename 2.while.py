conta=int(input("Insira o valor da conta: "))
juros=float(input("Insira a taxa de juros: "))
anos=int(input("Ano apos o deposito: "))
print(f"O valor da conta inicial: {conta}")
counter=1
while counter<=anos:
    counter+=1
    lucro=conta*juros
    conta+=lucro
    ano_final=counter-1
print(f"Ao fim do ano {ano_final} o valor da conta: {conta}")
