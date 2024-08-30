dinheiro = float(input())
horas = int(input())
salario_bruto = dinheiro * horas
ir = salario_bruto * (11/100)
inss = salario_bruto * (8/100)
sindicato = salario_bruto * (5/100)
descontos = ir + inss + sindicato
salario_liquido = salario_bruto - descontos
print(f'Seu salario bruto é R${salario_bruto}\nO imposto de renda é de R${ir}\nO desconto de inss é de R${inss}\nE de sindicato é de R${sindicato}\nTotalizando R${descontos} de desconto\nE seu salario liquido final é R${salario_liquido}')