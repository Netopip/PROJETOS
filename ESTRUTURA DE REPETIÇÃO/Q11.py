def intervalo(num1, num2):
    lista = list(range(num1,num2))
    soma = sum(lista)
    return soma




def main():
    num1 = int(input())
    num2 = int(input())

    msg = intervalo(num1, num2)
    print(msg)

if __name__ == '__main__':
    main()
