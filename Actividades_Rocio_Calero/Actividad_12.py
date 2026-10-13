from numpy import random

print('---ADIVINA EL NUMERO SECRETO---')
print('He pensado un numero secreto entre 0 y 10. Tienes 3 intentos')

secreto = random.randint(10)
intentos = 3
acertado = False

while intentos > 0 and not acertado:
    num = int(input('Introduzca un numero: '))
    intentos -= 1
    
    if num == secreto:
        acertado = True 
    elif num < secreto:
        print('El número secreto es MAYOR. Te quedan', intentos, 'intentos.')
    else:
        print('El número secreto es MENOR. Te quedan', intentos, 'intentos.')

if acertado:
    print('¡Enhorabuena! Has ganado')
else:
    print('Lo siento, has perdido. El número secreto era', secreto)