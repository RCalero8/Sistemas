print('Cajero automatico')

saldo = 210000.00
opcion = 1
while saldo != 0 and opcion != 0 :
    print ('Hola elija una opcion del cajero (1- Ver saldo, 2- Retirar dinero, 3- Comprar entradas, 4- Ingresar dinero, 0- Salir)')
    opcion = int(input('Elija la opcion que quiere: '))
    if opcion == 0:
        print('Salir')
    elif 1 < opcion > 4 :
        print('Elija una opcion correcta') 
    else:
        match opcion:
            case 1:
                print(f'Su saldo es de {saldo} €')
            case 2: 
                print('Que cantidad de dinero desea retirar')
                retiro = float(input('Introduzca la cantidad: '))
                saldo -= retiro
                if saldo == 0:
                    print('No le queda dinero en la cuenta.')       
                else:
                    print(f'Le queda est saldo {saldo} ')
            case 3:
                print('Desea comprar una entrada')
                entrada = float(input('Introduzca el precio de la entrada: '))
                saldo -= entrada
                if saldo == 0:
                    print('No le queda dinero en la cuenta.')       
                else:
                    print(f'Le queda est saldo {saldo} ')
            case 4: 
                print('Que cantidad de dinero desea ingresar')
                añado = float(input('Introduzca la cantidad: '))
                saldo += añado
                print(f'Su saldo es de {saldo}')