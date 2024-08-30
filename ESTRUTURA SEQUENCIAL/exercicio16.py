
import math
area = float(input('Quantos M² você quer pintar: '))
litros = area / 3
latas = math.ceil(litros / 18)#a função ceil aproxima o numero de ponto flutuante para cima(mais)
custo = math.ceil(latas * 80)
print(f'A quantidade de latas a serem compradas para cobrir a area de {area}m² é de {latas} latas\nE o custo total é de R${custo}')
