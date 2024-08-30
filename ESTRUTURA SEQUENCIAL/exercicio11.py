def calcular_numeros(a, b, c):
    produto = (a * 2 ) * (b/2)
    soma = (a * 3) + (c)
    cubo = (c**3)
    return [produto, soma, cubo]

def main():
    n1 = int(input('Digite o 1º numero: '))
    n2 = int(input('Digite o 2º numero: '))
    n3 = float(input('Digite o 3º numero: '))

    produto, soma, cubo = calcular_numeros(n1, n2, n3)

    print(f'O resultados das operações:(a * 2 ) * (b/2) é {produto}\nO resultado de (a * 3) + (c) é {soma}\nE (c**3) é {cubo}.')

if __name__ == '__main__':
    main()