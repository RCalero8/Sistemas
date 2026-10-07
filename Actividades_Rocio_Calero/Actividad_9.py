print('---RECOPILADOR DE PALABRAS---')
palabras = []

texto = input('Escribe una palabra (o pulsa Enter para terminar):')

#Bucle hasta que este vacio
while texto != '':
    palabras.append(texto)
    texto = input('Escribe una palabra (o pulsa Enter para terminar):')
#Mostrar el listado
print('Estas son las palabras que has escrito: ')
for palabra in palabras:
    print(palabra)