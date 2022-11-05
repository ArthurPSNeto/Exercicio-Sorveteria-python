#Sorveteria

preco=0
op=0        
print("Ola, somos uma sorveteria. Nos temos 2 tipos de sorvete: Premium e Comum. O premium custa R$20,00 e o comum custa R$ 15,00\n1 - Sorvete premium\n2 - Sorvete comum\n")
preco=int(input("\nQual tipo de sorvete você vai querer?\n"))
if preco==1:
    preco=20
else:
    preco=15

op=int(input("\nNos vendemos o sorvete em copinho ou em casquinha. O valor da casquinha e R$2,00 e o valor do copinho e R$1,00. Qual recipiente você vai escolher?\n1 - Copinho:\n2 - Casquinha:\n"))
if op==1:
    
    preco=preco+1
else:
    preco=preco+2

op=int(input("\nA cobertura pode ser apenas uma por R$1 ou cobertura especial(mais de uma) por apenas R$2,00. Qual você vai querer?\n1 - Simples\n2 - Especial\n"))
if op==1:
    preco=preco+1
else:
    preco=preco+2

print("\nVocê vai pagar: ",preco)
