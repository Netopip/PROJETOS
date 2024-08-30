
import math
area = float(input('Quantos M² você quer pintar: '))
litros = area / 6
latas = math.ceil(litros / 18)
custo = math.ceil(latas * 80)
galoes = math.ceil(litros / 3.6)
custo_ga = math.ceil(galoes * 25)

print(f'Se voce comprar latas para pintar uma área de {area}m², voce precisara de {latas} lata o que custará R${custo} '
      f'e se voce prefirir galoes voce precisará de {galoes} e o custo total é de R${custo_ga}')
