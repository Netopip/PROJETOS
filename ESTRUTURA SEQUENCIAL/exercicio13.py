

while True:
    altura = float(input('Digite a sua altura: '))
    sexo = str(input('Qual o seu sexo:[M/F] ')).upper().strip()
    if sexo == 'M':
        ideal = (72.7 * altura) - 58
        print(f'O seu peso ideal é de {ideal:.2f}')
    elif sexo == 'F':
        ideal = (62.1 * altura) - 44.7
        print(f'O seu peso ideal é de {ideal:.2f}')
    else:
        print('Digite algo válido.')
    while True:
        resp = str(input('Voce quer continuar:[S/N] ')).upper().strip()
        if resp == 'S':
            print('Vamos continuar!')
            break
        elif resp == 'N':
            break
        else:
            print('Digite algo valido.')
    if resp == 'N':
        break

print('Encerramos por aqui')




