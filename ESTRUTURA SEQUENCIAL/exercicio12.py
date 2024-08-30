
while True:
    altura = float(input('Digite a sua altura: '))
    ideal = (72.7 * altura) - 58
    print(f'O seu peso ideal é {ideal:.2f}')
    while True:
        res = str(input('Quer continuar(S para sim e N para Não). ')).upper().strip()
        if res in 'Ss':
            print('vamos continuar!')
            break
        elif res in 'Nn':
            break
        else:
            print('Digite algo válido!')
    if res == 'N':
        break

print('Acabamos por aqui!')

