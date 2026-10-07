print('---SUMAR HASTA LLEGAR AL OBJETIVO---')

objetivo = int(input('Escribe un número entero: '))

numeros = []
suma = 0

#Bucle para la suma
while suma < objetivo:
    entrada = int(input('Escribe otro número entero: '))
    numeros.append(entrada)
    suma = suma + entrada

print('Has llegado al objetivo.')
print('La suma es:', suma)
print('Estos son los números que has escrito:')
#Bucle para listar los numeros
for numero in numeros:
    print(numero)