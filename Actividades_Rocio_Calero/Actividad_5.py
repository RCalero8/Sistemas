n1 = input('Introduzca un numero: ')
if (num1 := int(n1)) < 10 and (num1 := int(n1)) > 0:
    print(num1, ' esta entre 0 y 10')
else:
    print(num1, ' esta fuera de 0 y 10')