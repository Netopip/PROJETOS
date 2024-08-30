
def main():
    while True:
        usuario = str(input())
        senha = str(input())
        if usuario != senha:
            print('Usuario e senhas validas!')
            break
        else:
            print('Erro. O usuairo não pode ser igual a senha!')

    print('Fim')

if __name__ == '__main__':
    main()