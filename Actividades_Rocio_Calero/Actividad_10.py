print('---RECOPILADOR DE NUMEROS---')
numeros = []

numerador = input('Escribe un numero (o pulsa Enter para terminar):')

#Bucle hasta que este vacio
while numerador != '':
    numeros.append(int(numerador))
    numerador = input('Escribe un numero (o pulsa Enter para terminar):')
#Mostrar el listado
print('Estas son las palabras que has escrito: ')
for numero in numeros:
    print(numero)