#Calculadora
print('Calculadora')

opcion = 1
while opcion != 0:
    print ('Hola elija una opcion de la calculadora (1- Suma, 2- Resta, 3- Multiplicacion, 4- Division, 5- Resto, 0- Salir)')
    opcion = int(input('Elija la opcion que quiere: '))
    if opcion == 0:
        print('Salir')
    elif 1 < opcion > 5 :
        print('Opcion no valida')
    else:
        num1 = float(input('Introduzca el 1º numero: '))
        num2 = float(input('Introduzca el 2º numero: '))
        match opcion:
            case 1:
                resultado = num1 + num2
                print(f'{num1} + {num2} = {resultado}')
            case 2:
                resultado = num1 - num2
                print(f'{num1} - {num2} = {resultado}')
            case 3:
                resultado = num1 * num2
                print(f'{num1} x {num2} = {resultado}')
            case 4:
                if num2 != 0:
                    resultado = num1 // num2
                    print(f'{num1} / {num2} = {resultado}') 
                else:
                    print('No se puede dividir por 0')
            case 5:              
                print('Resto: ')
                if num2 != 0:
                    resultado = num1 % num2
                    print(f'{num1} % {num2} = {resultado}') 
                else:
                    print('No se puede dividir por 0')
