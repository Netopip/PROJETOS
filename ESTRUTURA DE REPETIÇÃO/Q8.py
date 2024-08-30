def soma(lista):
    maior = max(lista)
    return maior


def main():
    lista = list()
    for i in range(5):
        numero = int(input())
        lista.append(numero)
    ordem = sorted(lista)
    print(ordem)
    msg = soma(lista)
    print(msg)

if __name__ == '__main__':
    main()


