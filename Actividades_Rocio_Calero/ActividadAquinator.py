volar = input('¿Puede volar? (si/no)')

if volar == 'si':
    humano = input('¿Es humano? (si/no)')
    if humano == 'si':
        mascara = input('¿Tiene mascara? (si/no)')
        if mascara == 'si':
            print('Iroman')
        else:
            print('Capitana Marvel')
    else:
        mascara1 = input('¿Tiene mascara?')
        if mascara1 == 'si':
                print('Ronan Accuser')
        else:
                print('Vision')
else:
    humano = input('¿Es humano? (si/no)')
    if humano == 'si':
        mascara = input('¿Tiene mascara? (si/no)')
        if mascara== 'si':
            print('Spiderman')
        else:
            print('Hulk')
    else:
        mascara1 = input('¿Tiene mascara? (si/no)')
        if mascara1 == 'si':
            print('Black Bolt')
        else:
            print('Thanos')