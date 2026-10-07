import numpy as np

print('---ADIVINA EL NÚMERO---')
print('He pensado un número entre 0 y 10. Tienes 3 intentos.')

secreto = np.random.randint(0, 11)
intentos = 3
acertado = False

while intentos > 0 and acertado == False:
    numero = int(input('Escribe un numero: '))
    intentos = intentos - 1

    if numero == secreto:
        acertado = True
    elif numero < secreto:
        print('Es mayor. Te quedan', intentos, 'intentos.')
    else:
        print('Es menor. Te quedan', intentos, 'intentos.')

if acertado:
    print('¡Enhorabuena, has acertado!')
else:
    print('Has perdido. El número era', secreto)