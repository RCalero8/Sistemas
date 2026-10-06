n1 = input('Introduzca un numero: ')
if (num1 := int(n1)) < 10 and (num1 := int(n1)) > 0:
    print(num1, ' esta entre 0 y 10')
elif (num1 := int(n1)) < 20 and (num1 := int(n1)) > 11:
    print(num1, ' esta entre de 11 y 20')
elif (num1 := int(n1)) < 30 and (num1 := int(n1)) > 21:
    print(num1, ' esta entre 21 y 30')
else: 
    print(num1, ' esta fuera de 0 y 10')
