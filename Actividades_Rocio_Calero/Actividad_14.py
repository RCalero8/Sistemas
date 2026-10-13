print('---CREADOR DE TRIANGULO---')

numero = int(input('Introduzca un numero para crear un triangulo de asteriscos (*): '))

for i in range(1, numero + 1, 1):
    print('*' * i)

for j in range(numero - 1, 0, -1):
    print('*' * j)
    