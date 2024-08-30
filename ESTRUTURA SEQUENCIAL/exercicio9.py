def transformar_temp(temp):
    c = 5 * ((temp- 32)/ 9)
    return c

def main():
    fahrenheit = float(input('Digite a temperatura em graus Fahrenheit:'))

    resultado = transformar_temp(fahrenheit)
    print(f'O resultado da transformação da temperatura {fahrenheit}F em graus celsius é de {resultado:.2f}ºC')

if __name__ == '__main__':
    main()