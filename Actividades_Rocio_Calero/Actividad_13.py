print('---CALCULADORA DE FACTORIAL---')

numero = int(input('Escribe un numero: '))

resultado = 1

for i in range(1, numero + 1):
    resultado = resultado * i
print ('El factorial de ', numero, ' es ',resultado)