#Repetir cadenas (Utilizamos el operador *)
print('REPETIR CADENAS')
repetir = 'Hola'
print(repetir*5)

#Obtener un carater
print('*******************')
print('OBTENER UN CARACTER')
sentence = 'Hola, mundo'
print(sentence[0])
print(sentence[-1])
print(sentence[4])
print(sentence[-5])

#Trocear una cadena
print('*******************')
print('TROCEAR UNA CADENA')
proverb = 'Agua pasada no mueve molino'
print(proverb[:]) #Copia toda la cadena
print(proverb[12:]) #Extrae desde el caracter 12
print(proverb[:11]) #Extrae hasta el caracter 11
print(proverb[5:11]) #Extrae desde el caracter 5 al caracter 11
print(proverb[5:11:2]) #Tomar un trozo de una lista o texto, desde una posición inicial (start) hasta antes de llegar a la final (end), dando saltos de varios pasos a la vez (step).

#Longitud de una cadena
print('*******************')
print('LONGITUD DE UNA CADENA')
proverb1 = 'Lo cortés no quita lo valiente'
print(len(proverb1))
empty = ''
print(len(empty))

#Pertenencia de un elemento
print('*******************')
print('PERTENENCIA DE UN ELEMENTO')
proverb2 = 'Más vale malo conocido que bueno por conocer'
print('malo' in proverb2)
print('bueno' in proverb2)
print('regular' in proverb2)
dna_sequence= 'ATGAAATTGAAATGGGA'
print(not('C' in dna_sequence)) #Primera aproximación
print('C' not in dna_sequence)  #Forma pitónica

#Dividir una cadena
print('*******************')
print('DIVIDIR UNA CADENA')
proverb3= 'No hay mal que por bien nno venga'
print(proverb3.split())
tools = 'Martillo, Sierra, Destornillador'
print(tools.split(','))

#Limpiar cadena
print('*******************')
print('LIMPIAR CADENA')
serial_number = '\n\t   \n 48374983274832      \n\n\t   \t   \n'
print(serial_number.strip())
print('Left strip' + serial_number.lstrip())
print('Right strip' + serial_number.rstrip())
print('Borrado de n' + serial_number.strip('\n'))

