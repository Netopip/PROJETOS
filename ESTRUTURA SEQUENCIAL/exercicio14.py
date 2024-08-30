

peso = float(input())
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print(f'Voce excedeu o peso limite em {excesso}Kg, por isso voce esta sendo multado em R${multa}')
else:
    print(f'Voce esta com {peso}kg, peso dentro do limite de 50kg!')