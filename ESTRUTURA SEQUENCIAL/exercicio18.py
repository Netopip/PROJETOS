

mb_arquivo = float(input('Qual o tamanho do arquivo: [Mb] '))
velocidade = float(input('Qual a velocidade da internet: [Mb/s]'))
tempo = mb_arquivo / velocidade
minutos = tempo / 60
print(f'Você ira terminar o download em {minutos:.3f} minutos ou em {tempo} segundos.')




